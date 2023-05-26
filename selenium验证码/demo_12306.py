from selenium import webdriver
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

option.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=option)
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
driver.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys("19896278773")
driver.find_element(By.XPATH,'//*[@id="J-password"]').send_keys("zhou1234")
driver.find_element(By.XPATH,'//*[@id="J-login"]').click()
time.sleep(2)

btn = driver.find_element(By.XPATH,'//*[@id="nc_1_n1z"]')

ActionChains(driver).drag_and_drop_by_offset(btn,300,0).perform()