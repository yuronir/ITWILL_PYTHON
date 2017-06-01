import urllib.request
from  bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

KEYWORD = '포켓몬'

binary = 'D:\chromedriver/chromedriver.exe'
driver = webdriver.Chrome(binary)
driver.get("https://www.instagram.com/explore/")
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("kasrtrn@naver.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("ewq123")
driver.find_element_by_name("password").submit()

# 검색어 입력
driver.get("https://www.instagram.com/explore/")
driver.find_element_by_css_selector("div._etslc").click()
elem = driver.find_element_by_css_selector("input._9x5sw._qy55y")
elem.clear()
elem.send_keys(KEYWORD)
time.sleep(10)
elem.send_keys(Keys.ENTER)
time.sleep(10)
# 반복할 횟수
for i in range(1, 3):
    driver.find_element_by_xpath("//body").send_keys(Keys.END)
    time.sleep(5)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "lxml")

def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="_icyx7")
    for im in imgList:
        params.append(im["src"])
    return params
    # print(params)

def fetch_detail_url():
    params = fetch_list_url()
    # print(params)
    a = 1
    for p in params:
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve(p, "D:/web_croll/instagramimage/" + KEYWORD + "/" + str(a) + ".jpg")
        # download_web_images(p,'d:\');
        a = a + 1

fetch_detail_url()
driver.quit()