import  urllib.request
from  bs4  import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


binary = 'D:\chromedriver/chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get("http://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=")
elem = browser.find_element_by_id("q")
# find_elements_by_class_name("")


# 검색어 입력
elem.send_keys("햄버거")
elem.submit()


# 반복할 횟수
for i in range(1 ,3):
    browser.find_element_by_xpath("//body").send_keys(Keys.END)
    time.sleep(20)


time.sleep(20)
html = browser.page_source
soup = BeautifulSoup(html ,"lxml")

# print(soup)
# print(len(soup))


def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="thumb_img")
    for im in imgList:
        params.append(im["src"])
    return params



def  fetch_detail_url():
    params = fetch_list_url()
    print(params)
    a = 1
    for p in params:
        print (p)
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve(p, "d:/daumImages/"+ str(a) + ".jpg")
        a = a + 1

fetch_detail_url()
browser.quit()

