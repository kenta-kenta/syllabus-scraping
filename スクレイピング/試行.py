from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import csv
import datetime

options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://ku-portal.kyushu-u.ac.jp/campusweb/slbssbdr.do?value(risyunen)=2023&value(semekikn)=1&value(kougicd)=23535204&value(crclumcd)=ZZ')

sleep(1)
element = driver.find_element_by_xpath('''//td[text()='" テキスト "']''')

# テキストを取得
text = element.text
print(text)