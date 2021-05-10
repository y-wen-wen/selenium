#coding = utf-8
import pytest
from selenium import webdriver
from time import sleep, ctime
import os
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"

chrome_driver_binary = "C:\\Users\\Lenovo\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary,chrome_options=options)

class TestCase():
    def setup_class(self):
        print("start")

    def teardown_class(self):
        print("end ")
        driver.quit()

    def setup_method(self):

        driver.get("http://www.baidu.com")
        sleep(3)

    def teardown_method(self):
        sleep(3)

    def test_one(self):
        print(1)
        driver.find_element_by_id("kw").send_keys("Test search")
        driver.find_element_by_id("su").click()
        sleep(3)

    def test_two(self):
        #空格
        driver.find_element_by_id("kw").send_keys(" ")
        driver.find_element_by_id("su").click()
        sleep(3)
    def test_three(self):
        #数字
        driver.find_element_by_id("kw").send_keys("123456")
        driver.find_element_by_id("su").click()
        sleep(3)
    def test_four(self):
        #中文字符串
        driver.find_element_by_id("kw").send_keys("开心")
        driver.find_element_by_id("su").click()
        sleep(3)
    def test_five(self):
        #符号
        driver.find_element_by_id("kw").send_keys("!")
        driver.find_element_by_id("su").click()
        sleep(3)
    #用不同控件查找方法：
    def test_six(self):
        driver.find_element_by_link_text("hao123").click()
        sleep(3)
    def test_seven(self):
        driver.find_element_by_link_text("学术").click()
        sleep(3)
