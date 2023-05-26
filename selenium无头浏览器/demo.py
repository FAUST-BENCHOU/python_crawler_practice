from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_argument("--headless")
option.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=option)
driver.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

sel_el = driver.find_element(By.XPATH,'//*[@id="OptionDate"]')

sel = Select(sel_el)

for i in range(len(sel.options)):
    sel.select_by_index(i)
    time.sleep(2)
    table = driver.find_element(By.XPATH,'//*[@id="TableList"]/table')
    print(table.text)
    print("++++++++++++++++++++++++++++++++")

driver.close()
