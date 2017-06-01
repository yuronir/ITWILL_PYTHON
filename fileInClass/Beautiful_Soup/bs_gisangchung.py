# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import operator
import time


class KMACrawler:
    FILE_PATH = 'D:\\web_croll\\'

    def __init__(self):
        self.location_list = {}
        self.year_list = {}
        self.factor_list = {}
        self.crawling_list = {}
        self.data = {}
        self.default_url = 'http://www.kma.go.kr/weather/climate/past_table.jsp'
        self.crawled_url = 'http://www.kma.go.kr/weather/climate/past_table.jsp?stn={}&yy={}&obs={}'

    def crawling(self):
        self.get_kma_data()
        self.play_crawling()

    # 지점, 연도, 요소에 데이터 가져오는 함수
    def get_kma_data(self):
        # 메인url을 통해 html 코드를 가져오는 부분
        res = urlopen(Request(self.default_url)).read()
        soup = BeautifulSoup(res, 'html.parser')

        location = soup.find('select', id='observation_select1')
        year = soup.find('select', id='observation_select2')
        factor = soup.find('select', id='observation_select3')

        for tag in location.find_all('option'):
            if tag.text != '--------':
                self.location_list[tag['value']] = tag.text
                # print(tag['value']) # 188
                # print(tag.text)     # 성산(무)
        for tag in year.find_all('option'):
            if tag.text != '--------':
                self.year_list[tag['value']] = tag.text
                # print(tag['value']) #  1961
                # print(tag.text)     #  1961
        for tag in factor.find_all('option'):
            if tag.text != '--------':
                self.factor_list[tag['value']] = tag.text
                # print(tag['value']) #평균풍속
                # print(tag.text)     # 12
        # print(self.location‎_list.items())
        # print(self.year_list.items())
        # print(self.factor_list.items())

        # location_list, year_list, factor_list(셋 다 select box)로 가능한 모든 조합 담기
        # 주소값(stn, yy, obs)에 하나하나 넣으면서 페이지 열고 값 얻어내기 위한 용도
        for loc_key, loc_value in self.location_list.items():
            for year_key, year_value in self.year_list.items():
                for fac_key, fac_value in self.factor_list.items():
                    self.crawling_list[(loc_key, year_key, fac_key)] = (loc_value, year_value, fac_value)

        # print(self.crawling_list)

    # 크롤링 수행하는 메인 함수
    def play_crawling(self):
        print('크롤링을 위한 데이터를 수집 중입니다...')
        # self.crawling_list = {('258', '2015', '35'): ('보성군(무)', '2015', '일조시간')}
        print('크롤링을 위한 데이터 수집 완료 !!!')
        print('크롤링을 시작합니다...')
        for key, value in sorted(self.crawling_list.items(), key=operator.itemgetter(0)):
            res = urlopen(Request(self.crawled_url.format(key[0], key[1], key[2]))).read()
            soup = BeautifulSoup(res, 'html.parser')
            print('현재 키워드 : {}, {}, {}'.format(*value))
            for tr_tag in soup.find('table', class_='table_develop').find('tbody').find_all('tr'):
                if self.data.get(value) is None:
                    self.data[value] = []
                self.data[value].append(['' if td_tag.text == '\xa0' else td_tag.text for td_tag in tr_tag.find_all('td') if td_tag.has_attr('scope') is False])
                # td.tag : [<td scope="row">1일</td>, <td> </td>, <td> </td>, <td> </td>, <td> </td>, <td> </td>, <td> </td>, <td> </td>, <td> </td>, <td> </td>, <td> </td>, <td> </td>, <td> </td>]
            print('{}, {}, {} 에 대한 데이터 저장...'.format(*value))
            self.data_to_file()
            self.data.clear()
            print('저장 완료!!!\n\n')
            time.sleep(2)
        print('크롤링 완료 !!!')

    # 크롤링 된 데이터를 파일로 저장하는 함수
    def data_to_file(self):
        with open(KMACrawler.FILE_PATH + "kma_crawled.txt", "a", encoding="utf-8") as file:
            file.write('======================================================\n')
            for key, value in self.data.items():
                file.write('>> ' + key[0] + ', ' + key[1] + ', ' + key[2] + '\n')
                for v in value:
                    file.write(','.join(v) + '\n')
            file.write('======================================================\n\n')
            file.close()

crawler = KMACrawler()
crawler.crawling()