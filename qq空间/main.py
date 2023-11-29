
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import jiexi
import pyautogui
driver = Edge()
# yourqq写你的QQ号
driver.get("https://user.qzone.qq.com/2319109590/infocenter")
time.sleep(10) #在这10s内你要人工登录
for i in range(10000):
	time.sleep(1)
	# 使用 WebDriverWait 来等待元素出现
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*"))
	)

	html = element.get_attribute("outerHTML")
	# 解析html
	jiexi.get(html)
	pyautogui.scroll(-7500)
	# 向下滑动
	# time.sleep(1)
driver.close()
