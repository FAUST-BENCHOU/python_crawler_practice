from selenium import webdriver
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
#option.add_argument("--headless")
#option.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=option)
driver.get('https://www.chaojiying.com/user/login/')
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("zhou1111")
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("zhou1234")

img = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('zhou1111', 'zhou1234', '947044')	#用户中心>>软件ID 生成一个替换 96001
												#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()