from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime
import ssl
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager




path = '/home/sanghoon/Documents/Develop/chromedriver'

driver = webdriver.Chrome(executable_path=path)


driver.get(url="http://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchMain.do")
# # html= browser.find_element_by_xpath(".//html")
elements = driver.find_elements(By.XPATH, '//*[@id="main_contents"]/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]')
# p_element = driver.find.elements_by_tag_name("p")
# print(p_element[10].text)
# <p class="tit">엔진 개발자 모집</p>
print(type(elements), elements)
# # <class 'list'> [<selenium.webdriver. ..., -8638-2f7617332c69")>]
# # //*[@id="main_contents"]/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div[1]/a/p[2]
# # //*[@id="main_contents"]/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div[2]/a/p[2]
# # //*[@id="main_contents"]/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div[1]/a/div/p[2]
for e in elements:
    if e != None:
        print(type(e.text), repr(e.text))
#         # <class 'str'> <a ...
#         # <class 'str'> <a ...

req = driver.page_source
# res = requests.get('http://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchMain.do')
# if res.status_code == 200:
soup = BeautifulSoup(req, 'html.parser')
links = soup.find_all('p', class_='link_txt')
print('task_crawling_worknet : ', type(links), len(links))
dates = list()
name = str()
tit = str()
right = str()
for link in links:
    title = str.strip(link.get_text())
    link = link.get('href')
    data = {"name": name, "tit": tit, "etc":etc, "create_date": datetime.datetime.now()}
    dates.append(data)

with MongoClient('mongodb://192.168.219.128:27017/')  as client: 
    mydb = client.mydb
    req = mydb.worknet.insert_many(dates)