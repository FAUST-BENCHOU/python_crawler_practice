from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
#option.add_argument("--headless")
#option.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=option)
driver.get('https://www.zhipin.com/shanghai/')

time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/div[2]/p/input').send_keys("python",Keys.ENTER)

driver.find_element(By.XPATH,'//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div[1]/a/div[1]/span[1]').click()
job_name = driver.find_element(By.XPATH,'//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div[1]/a/div[1]/span[1]')
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
job_detail = driver.find_element(By.XPATH,'//*[@id="main"]/div[3]/div/div[2]/div[1]/div[2]').text
print(job_name.text)
print(job_detail)

driver.close()
driver.switch_to.window(driver.window_handles[0])