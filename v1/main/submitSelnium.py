# -*- coding: utf8 -*-
'''
@Author : huangrenwu
@File: submitSelnium.py
@Time: 2022/7/12 9:11
@Email: leo.r.huang@microcore.tech
@Desc: 
'''

from selenium import webdriver


driver = None

class Test:
    def main(self):
        global driver
        driver = webdriver.Chrome(executable_path=r'D:/Project/submitProject/file/chromedriver.exe')
        driver.maximize_window()
        driver.get("https://www.baidu.com")

if __name__ == '__main__':
    Test().main()