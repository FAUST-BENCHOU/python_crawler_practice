from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get('https://1.tongji.edu.cn/')

driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("")
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("")

driver.find_element(By.XPATH,'//*[@id="reg"]').click()

my_point = driver.find_element(By.XPATH,'//*[@id="mpanel5"]/div/div/div[2]/div/div[2]/span')
click_points = my_point.text.split("【")[1].split("】")[0].split(",")
print(click_points)



verify_img_ele = driver.find_element(By.XPATH,'//*[@id="mpanel5"]/div/div/div[2]/div/div[1]/div/img')
chaojiying = Chaojiying_Client('zhou1111', 'zhou1234', '947044')
dic = chaojiying.PostPic(verify_img_ele.screenshot_as_png, 9004)
result = dic['pic_str']
print(dic)
print(result)
