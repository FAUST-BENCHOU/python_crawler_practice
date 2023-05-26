from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get('https://lagou.com')
driver.find_element(By.XPATH,'//*[@id="changeCityBox"]/ul/li[2]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)

job_list = driver.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')


print(job_list)
for job in job_list:
    job_name = job.find_element(By.XPATH,'//*[@id="openWinPostion"]').text
    #/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/span/div/div[1]/a
    print(job_name)

