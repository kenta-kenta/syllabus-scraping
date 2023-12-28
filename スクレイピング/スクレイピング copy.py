from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import csv
import datetime
driver = webdriver.Chrome('C:\\Users\\kenke\\Downloads\\スクレイピング\\chromedriver.exe')

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('C:\\Users\\kenke\\Downloads\\スクレイピング\\chromedriver.exe',options=options)
driver.get('https://ku-portal.kyushu-u.ac.jp/campusweb/slbsskgr.do?clearAccessData=true&contenam=slbsskgr&kjnmnNo=7')

#一覧を大きくする
driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/form/div[3]/table[2]/tbody/tr[5]/td[3]/input[1]").click()
select1 = Select(driver.find_element_by_name("value(kaikoCd)"))

#開講時期選択
select1.select_by_index(9) 

#開講学部選択
driver.find_element_by_id('工学部').click()

dropdown = driver.find_element_by_name("maxDispListCount")
select = Select(dropdown)
select.select_by_index(6) #最大表示量

#ファイルについて
csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = '練習' + csv_date + '.csv'
f = open(csv_file_name, 'w', encoding='cp932', errors='ignore')
writer = csv.writer(f, lineterminator='\n') 
csv_header = ["整理番号","科目名","担当教諭","教科書",]
writer.writerow(csv_header)

item = 1
for Num in range(3,5):
    csvlist = []
    csvlist.append(str(item))
    driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/table/tbody/tr/td[1]/form/div[4]/table/tbody/tr[{Num}]/td[3]/a').click()
    csvlist.append(driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/div[2]/form/div[2]/table/tbody/tr[2]/td[3]").text) #科目名
    if driver.find_elements_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/div[2]/form/div[2]/table/tbody/tr[6]/td[3]/p"):
        csvlist.append(driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/div[2]/form/div[2]/table/tbody/tr[6]/td[3]/p").text) #担当教諭
    if driver.find_elements_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/div[2]/form/div[2]/table/tbody/tr[8]/td[3]/p"):
        csvlist.append(driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/div[2]/form/div[2]/table/tbody/tr[8]/td[3]/p").text) #担当教諭
    #csvlist.append(driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[1]/div[2]/form/div[3]/table/tbody/tr[24]/td[3]/table/tbody/tr/td").text)
    if driver.find_elements_by_xpath('/html/body/div/div[2]/table/tbody/tr/td[1]/div[2]/form/div[3]/table/tbody/tr[26]/td[3]/table/tbody/tr/td'):
        csvlist.append(driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[1]/div[2]/form/div[3]/table/tbody/tr[26]/td[3]/table/tbody/tr/td").text)
    if driver.find_elements_by_xpath('/html/body/div/div[2]/table/tbody/tr/td[1]/div[2]/form/div[3]/table/tbody/tr[28]/td[3]/table/tbody/tr/td'):
        csvlist.append(driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[1]/div[2]/form/div[3]/table/tbody/tr[28]/td[3]/table/tbody/tr/td").text)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/div[2]/form/div[1]/table/tbody/tr/td/div/input").click()
    writer.writerow(csvlist)
    item = item + 1
    sleep(2)


