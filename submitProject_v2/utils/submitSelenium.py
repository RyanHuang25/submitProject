# -*- coding: utf8 -*-
'''
@Author : huangrenwu
@File: submitSelenium.py
@Time: 2022/7/12 16:47
@Email: leo.r.huang@microcore.tech
@Desc: 
'''
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SubmitUser:

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        try:
            self.driver = webdriver.Chrome(executable_path=r'/Users/huangrenwu/Project/submitProject/submitProject_v2/file/chromedriver',options=option)
        except:
            self.driver = webdriver.Chrome(executable_path=r'D:/Project/submitProject/file/chromedriver.exe',options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # self.driver.get('')

    def startRequest(self,data_list):
        '''
        数据结构：名字 电话 url
        :param data_list:
        :return:
        '''
        for data in data_list:
            infoList = data.split(' ')
            userName = infoList[0]
            userPhone = infoList[1]
            url = infoList[2]

            self.driver.execute_script(f"window.open('{url}')")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            if 'wanxinying' in url:
                self.chuangxin(userName,userPhone)
            elif 'jinshuju' in url:
                self.jinshuju(userName,userPhone)
            elif 'yongyushiyan' in url:
                self.maike(userName,userPhone)
        handless = self.driver.window_handles
        for hand in handless:
            self.driver.switch_to.window(hand)

    def chuangxin(self,userName,userPhone):
        self.driver.find_element_by_id("name").send_keys(userName)
        self.driver.find_element_by_id('telphone').send_keys(userPhone)
        self.driver.find_element_by_id('regBtn').click()

    def jinshuju(self,userName,userPhone):
        try:
            self.driver.find_element_by_xpath('//input[@name="field_3"]').send_keys(userName)
            self.driver.find_element_by_xpath('//input[@name="field_4"]').send_keys(userPhone)
            self.driver.find_element_by_xpath('//div[@class="published-form__footer-buttons"]/button').click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath('//input[@name="field_1"]').send_keys(userName)
            self.driver.find_element_by_xpath('//input[@name="field_2"]').send_keys(userPhone)
            self.driver.find_elements_by_xpath("//div[@class='ant-form-item-control-input-content']/span/div/div")[-1].click()
            self.driver.find_element_by_xpath('//div[@class="published-form__footer-buttons"]/button').click()
        except:
            pass

        try:
            # 判断网页是否提交成功
            Wait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "cashcow_root")))
            print(f'{userName} ===>>> 提交成功了')
        except:
            self.driver.refresh()
            self.jinshuju(userName, userPhone)

    def maike(self,userName,userPhone):
        try:
            self.driver.find_element_by_xpath('//input[@name="n"]').clear()
            self.driver.find_element_by_xpath('//input[@name="n"]').send_keys(userName)
            self.driver.find_element_by_xpath('//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').clear()
            self.driver.find_element_by_xpath('//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').send_keys(userPhone)
            try:
                selectList = self.driver.find_elements_by_xpath('//ul[@role="radiogroup"]/li')
                s = len(selectList) - 1
                status = True
                while s >= 0:
                    try:
                        if selectList[s].find_element_by_xpath('./span/span[2]').text == "配额已满":
                            s -= 1
                    except:
                        status = False
                        break
                if status:
                    title = self.driver.find_element_by_xpath('//div[@class="h_headline"]/span/span').text
                    print(f"麦克 ===>>> {title} ===>>> {userName} ===>>> 配额已满")
                    return
            except:
                pass
            self.driver.find_elements_by_xpath('//li[@class="fbc_optionsLi"]')[s].click()
            self.driver.find_element_by_xpath('//div[@class="submit"]/a').click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath('//input[@name="n"]').clear()
            self.driver.find_element_by_xpath('//input[@name="n"]').send_keys(userName)
            self.driver.find_element_by_xpath(
                '//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').clear()
            self.driver.find_element_by_xpath(
                '//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').send_keys(userPhone)
            try:
                selectList = self.driver.find_elements_by_xpath('//ul[@role="radiogroup"]/li')
                s = len(selectList) - 1
                status = True
                while s >= 0:
                    try:
                        if selectList[s].find_element_by_xpath('./span/span[2]').text == "配额已满":
                            s -= 1
                    except:
                        status = False
                        break
                if status:
                    title = self.driver.find_element_by_xpath('//div[@class="h_headline"]/span/span').text
                    print(f"麦克 ===>>> {title} ===>>> {userName} ===>>> 配额已满")
                    return
            except:
                pass
            self.driver.find_elements_by_xpath('//li[@class="fbc_optionsLi"]')[s].click()
            self.driver.find_element_by_xpath('//div[@class="submit"]/a').click()
        except:
            pass
        try:
            dataList = self.driver.find_elements_by_xpath('//input[@class="fbi_input aria-content"]')
            for data in dataList:
                data.clear()
            self.driver.find_elements_by_xpath('//input[@class="fbi_input aria-content"]')[0].send_keys(userName)
            self.driver.find_elements_by_xpath('//input[@class="fbi_input aria-content"]')[1].send_keys(userPhone)
            self.driver.find_element_by_xpath('//div[@class="submit"]/a').click()
        except:
            pass
        try:
            # 判断网页是否提交成功
            Wait(self.driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "fb_ssTitle")))
            print(f'{userName} ===>>> 提交成功了')
        except:
            self.driver.refresh()
            self.maike(userName, userPhone)

class SubmitUserMany:

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        try:
            self.driver = webdriver.Chrome(executable_path=r'/Users/huangrenwu/Project/submitProject/submitProject_v2/file/chromedriver',options=option)
        except:
            self.driver = webdriver.Chrome(executable_path=r'D:/Project/submitProject/file/chromedriver.exe',options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def startRequest(self,data_list):
        '''
        数据结构： 名字 电话 次数 url
        :param data_list:
        :return:
        '''
        for data in data_list:
            infoList = data.split(' ')
            userName = infoList[0]
            userPhone = infoList[1]
            count = int(infoList[2])
            url = infoList[3]

            # self.driver.execute_script(f"window.open('{url}')")
            # self.driver.switch_to.window(self.driver.window_handles[-1])
            if 'wanxinying' in url:
                print('创鑫不支持该功能')
            elif 'jinshuju' in url:
                self.count = 0
                self.jinshuju(userName,userPhone,count,url)
            elif 'yongyushiyan' in url:
                self.count = 0
                self.maike(userName,userPhone,count,url)
        handless = self.driver.window_handles
        for hand in handless:
            self.driver.switch_to.window(hand)

    def jinshuju(self,userName,userPhone,count,url):
        while count > self.count:
            try:
                self.driver.find_element_by_xpath('//input[@name="field_1"]').send_keys(userName)
                self.driver.find_element_by_xpath('//input[@name="field_2"]').send_keys(userPhone)
                self.driver.find_elements_by_xpath("//div[@class='ant-form-item-control-input-content']/span/div/div")[self.count].click()
                self.driver.find_element_by_xpath('//div[@class="published-form__footer-buttons"]/button').click()
            except:
                pass
            self.count += 1
            self.driver.execute_script(f"window.open('{url}')")
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def maike(self,userName,userPhone,count,url):
        while count > self.count:
            self.driver.execute_script(f"window.open('{url}')")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            try:
                self.driver.find_element_by_xpath('//input[@name="n"]').clear()
                self.driver.find_element_by_xpath('//input[@name="n"]').send_keys(userName)
                self.driver.find_element_by_xpath('//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').clear()
                self.driver.find_element_by_xpath('//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').send_keys(userPhone)
                try:
                    selectList = self.driver.find_elements_by_xpath('//ul[@role="radiogroup"]/li')
                    if selectList[self.count].find_element_by_xpath('./span/span[2]').text == "配额已满":
                        print(f"麦克 ===>>> {selectList[self.count].find_element_by_xpath('./span/span/span/span').text} ===>>> {userName} ===>>> 配额已满")
                except:
                    pass
                self.driver.find_elements_by_xpath('//li[@class="fbc_optionsLi"]')[self.count].click()
                self.driver.find_element_by_xpath('//div[@class="submit"]/a').click()
            except:
                pass

            self.count += 1

