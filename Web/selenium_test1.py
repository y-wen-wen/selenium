#coding = utf-8
from selenium import webdriver
from time import sleep, ctime
import os
options = webdriver.ChromeOptions()
#浏览可执行文件的地址：下载地址
options.binary_location = "C:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"
#浏览器驱动的下载地址
chrome_driver_binary = "C:\\Users\\Lenovo\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary,chrome_options=options)
#打开的网页
driver.get("http://www.baidu.com")
#找到id，模拟鼠标点击
driver.find_element_by_id("kw").send_keys("Test search")
driver.find_element_by_id("su").click()
#停3秒
sleep(3)
#退出
driver.quit()
