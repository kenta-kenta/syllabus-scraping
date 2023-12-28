from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import csv
import datetime

options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://ku-portal.kyushu-u.ac.jp/campusweb/slbsskgr.do?clearAccessData=true&contenam=slbsskgr&kjnmnNo=7')

driver.find_element_by_id('基幹教育').click()#開講学部選択
select1 = Select(driver.find_element_by_name("value(kaikoCd)"))
select1.select_by_index(3) #開講時期選択

#次のページに行く
elem1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/form/div[3]/div[2]/div/table/tbody/tr/td/div/input")
elem1.click()

dropdown = driver.find_element_by_name("maxDispListCount")
select = Select(dropdown)
select.select_by_index(6) #最大表示量


driver.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr/td[1]/form/div[4]/table/tbody/tr[3]/td[3]/a').click()
# 要素を見つける
element = driver.find_element_by_xpath('//td[text()="テキスト"]/following-sibling::td[3]')  # テキストが書かれている要素を取得

# テキストを取得
text = element.text
print(text)