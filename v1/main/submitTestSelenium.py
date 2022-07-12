# -*- coding: utf8 -*-
'''
@Author: huangrenwu
@File: submitTestSelenium.py
@Time: 2022/7/10 10:51
@Email: leo.r.huang@microcore.tech
'''

# 创鑫
chuangxin = {
    "chuangxinFalse": [
        'http://wanxinying.com:80/SubmitInfo/Index?token=on72O0HLstS%2bTrjMnWJuRAXKwhuTKJnjWqtLuQW0yE8pPqn9mCI1hEJzSUrgYMW3cWx%2f70zNL19BT5AMHm5SXl9BOg%2f3hgL0TZhWB7OWgAVXQoHtj07pn5Z7Gwx%2bSJuNYfzN2NypJn9PNZN9zLxBI1iEOH6dORa%2bo8rFTXKWp9c%3d',
        'http://wanxinying.com/SubmitInfo/Index?token=on72O0HLstS%2B7EaB16ZG2yC4qAYB0BsB5Rt83b2xdJnfesJPjTwg9k4LHGHeRZq7KvFsL7z3uuuuaYssrPTPCwufvWqKCUCzUeJpG8J6dPxaTadf7XsiVCBcOCUMm1Wlru00RC6PpyNR1oA0SfoHE9sUIPJOKVa2NXidIfcrBIeZg0smEs6qag%3D%3D',
        'http://wanxinying.com:80/SubmitInfo/Index?token=on72O0HLstQAtB0pNaoApuK1eUzYaOwO776KUwwbsDiBmRFsvFoWe634vMZVqAqqITdYGO1JiW6dz7RFch4488yHK4boWLxv3iLTSfF3dg97MpzyASGWW84l5%2bB3q8XVW9xemLL7YV0I7y6RxOfb9oJ6em87dpwU0L0XAPsRWQAWbY%2bjN6CGew%3d%3d'
    ]
}

# 金数据
jinshuju = {
    # 金数据没有选项的
    "jinshujuFalse": [
        'https://jinshuju.net/f/aM6GUI',
        'https://jinshuju.net/f/QU9mq1',
        'https://jinshuju.net/f/RnrZwN'
    ],
    # 金数据有选项的
    "jinshujuTrue": [
        'https://jinshuju.net/f/G7zcWi',
        'https://jinshuju.net/f/TZE1NX',
        'https://jinshuju.net/f/t7rPus'
    ]
}

maike = {
    # 麦克没有选项的
    "maikeFalse" : [
        'http://yongyushiyan.mikecrm.com/Jn6aZwM',
        'http://yongyushiyan.mikecrm.com/I1zwobw',
        'http://yongyushiyan.mikecrm.com/3Sa5QkT'
    ],
    # 麦克有选项的
    "maikeTrue" : {
        # 麦克有选项非必选
        "maikeTrueNot": [
            'http://yongyushiyan.mikecrm.com/WC5vJC1',
            'http://yongyushiyan.mikecrm.com/LcdzUov',
            'http://yongyushiyan.mikecrm.com/0F15NcX'
        ],
        # 麦克有选项必选
        "maikeTrueYes": [
            'http://yongyushiyan.mikecrm.com/0AeFGCX',
            'http://yongyushiyan.mikecrm.com/ql3KsfK',
            'http://yongyushiyan.mikecrm.com/SIyzPmT'
        ],
    },
    # 麦克仅在微信打开
    "maikeWechat": [
        'http://yongyushiyan.mikecrm.com/2DZ8p2U',
        'http://yongyushiyan.mikecrm.com/284qRnX',
        'http://yongyushiyan.mikecrm.com/ieYvWiF'
    ]
}

import random,time,threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = None

class SubmitMoney:

    def __init__(self):
        try:
            self.driver = webdriver.Chrome(executable_path=r'/Users/huangrenwu/Project/submitProject/file/chromedriver')
        except:
            self.driver = webdriver.Chrome(executable_path=r'D:/Project/submitProject/file/chromedriver.exe')
        self.driver.maximize_window()
        # self.driver.get('https://www.baidu.com')

        # hendlesList = self.driver.window_handles
        # for hendles in hendlesList:
        #     self.driver.switch_to.window(hendles)


    def startRequest(self,inputDate):
        # inputDate = input()
        data_list = inputDate.split(' ')
        url = data_list[0]
        userName = data_list[1]
        userAccount = data_list[2]
        print(f"name:{userName} === account:{userAccount}")
        self.driver.get(url)
        # self.driver.execute_script(f"window.open('{url}')")
        # hendlesList = self.driver.window_handles
        # if len(hendlesList) > 2:
        #     self.driver.switch_to.window(hendlesList[0])
        #     self.driver.close()

        # self.driver.switch_to.window(self.driver.window_handles[-1])

        print('-' * 100)
        if url in chuangxin['chuangxinFalse']:
            print(f'正在打开创鑫链接：{url}')
            self.chuangxin(userName,userAccount)
        elif url in jinshuju['jinshujuFalse']:
            print(f'正在打开金数据没有选项链接：{url}')
            self.jinshujuFalse(userName,userAccount)
        elif url in jinshuju['jinshujuTrue']:
            print(f'正在打开金数据有选项链接：{url}')
            self.jinshujuTrue(userName,userAccount)
        elif url in maike['maikeFalse']:
            print(f'正在打开麦克没有选项链接：{url}')
            self.maikeFalse(userName,userAccount)
        elif url in maike['maikeTrue']['maikeTrueNot']:
            print(f'正在打开麦克有选项非必须链接：{url}')
            self.maikeTrueNot(userName,userAccount)
        elif url in maike['maikeTrue']['maikeTrueYes']:
            print(f'正在打开麦克有选项必须链接：{url}')
            self.maikeTrueYes(userName,userAccount)
        elif url in maike['maikeWechat']:
            print(f'正在打开麦克微信链接：{url}')
            print('必须在微信中打开，跳过....')
        time.sleep(100)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
        print('-'*100)


    def chuangxin(self,userName,userAccount):
        # self.driver.get('http://wanxinying.com:80/SubmitInfo/Index?token=on72O0HLstS%2bTrjMnWJuRAXKwhuTKJnjWqtLuQW0yE8pPqn9mCI1hEJzSUrgYMW3cWx%2f70zNL19BT5AMHm5SXl9BOg%2f3hgL0TZhWB7OWgAVXQoHtj07pn5Z7Gwx%2bSJuNYfzN2NypJn9PNZN9zLxBI1iEOH6dORa%2bo8rFTXKWp9c%3d')
        self.driver.find_element_by_id("name").send_keys(userName)
        self.driver.find_element_by_id('telphone').send_keys(userAccount)
        self.driver.find_element_by_id('regBtn').click()
        time.sleep(2)
        # self.driver.close()
        # try:
        #     # 判断网页是否提交成功
        #     Wait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "xxx")))
        #     self.startRequest()
        # except:
        #     self.driver.refresh()
        #     self.chuangxin(userName,userAccount)

    def jinshujuFalse(self,userName,userAccount):
        # self.driver.get('https://jinshuju.net/f/aM6GUI')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//input[@name="field_3"]').send_keys(userName)
        self.driver.find_element_by_xpath('//input[@name="field_4"]').send_keys(userAccount)
        self.driver.find_element_by_xpath('//div[@class="published-form__footer-buttons"]/button').click()
        try:
            # 判断网页是否提交成功
            Wait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "cashcow_root")))
            print('提交成功了')
            # self.driver.close()
            # self.startRequest()
        except:
            self.driver.refresh()
            self.jinshujuFalse(userName,userAccount)

    def jinshujuTrue(self,userName,userAccount):
        # self.driver.get('https://jinshuju.net/f/G7zcWi')
        self.driver.find_element_by_xpath('//input[@name="field_1"]').send_keys(userName)
        self.driver.find_element_by_xpath('//input[@name="field_2"]').send_keys(userAccount)
        self.driver.find_elements_by_xpath("//div[@class='ant-form-item-control-input-content']/span/div/div")[-1].click()
        self.driver.find_element_by_xpath('//div[@class="published-form__footer-buttons"]/button').click()
        try:
            # 判断网页是否提交成功
            Wait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "cashcow_root")))
            print('提交成功了')
            # self.driver.close()
            # self.startRequest()
        except:
            self.driver.refresh()
            self.jinshujuFalse(userName, userAccount)

    def maikeFalse(self,userName,userAccount):
        # self.driver.get('http://yongyushiyan.mikecrm.com/Jn6aZwM')
        dataList = self.driver.find_elements_by_xpath('//input[@class="fbi_input aria-content"]')
        for data in dataList:
            data.clear()
        self.driver.find_elements_by_xpath('//input[@class="fbi_input aria-content"]')[0].send_keys(userName)
        self.driver.find_elements_by_xpath('//input[@class="fbi_input aria-content"]')[1].send_keys(userAccount)
        self.driver.find_element_by_xpath('//div[@class="submit"]/a').click()
        try:
            # 判断网页是否提交成功
            Wait(self.driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "fb_ssTitle")))
            print('提交成功了')
            # self.driver.close()
            # self.startRequest()
        except:
            self.driver.refresh()
            self.maikeFalse(userName, userAccount)

    def maikeTrueNot(self,userName,userAccount):
        # self.driver.get('http://yongyushiyan.mikecrm.com/WC5vJC1')
        self.driver.find_element_by_xpath('//input[@name="n"]').clear()
        self.driver.find_element_by_xpath('//input[@name="n"]').send_keys(userName)
        self.driver.find_element_by_xpath('//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').clear()
        self.driver.find_element_by_xpath('//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').send_keys(userAccount)
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
        self.driver.find_elements_by_xpath('//li[@class="fbc_optionsLi"]')[-1].click()
        self.driver.find_element_by_xpath('//div[@class="submit"]/a').click()
        try:
            # 判断网页是否提交成功
            Wait(self.driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "fb_ssTitle")))
            print('提交成功了')
            # self.driver.close()
            # self.startRequest()
        except:
            self.driver.refresh()
            self.maikeTrueNot(userName, userAccount)

    def maikeTrueYes(self,userName,userAccount):
        # self.driver.get('http://yongyushiyan.mikecrm.com/0AeFGCX')
        self.driver.find_element_by_xpath('//input[@name="n"]').clear()
        self.driver.find_element_by_xpath('//input[@name="n"]').send_keys(userName)
        self.driver.find_element_by_xpath('//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').clear()
        self.driver.find_element_by_xpath('//input[@class="fbi_input aria-content" ][@aria-invalid="false"]').send_keys(userAccount)
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
        self.driver.find_elements_by_xpath('//li[@class="fbc_optionsLi"]')[-1].click()
        self.driver.find_element_by_xpath('//div[@class="submit"]/a').click()
        try:
            # 判断网页是否提交成功
            Wait(self.driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "fb_ssTitle")))
            print('提交成功了')
            # self.driver.close()
            # self.startRequest()
        except:
            self.driver.refresh()
            self.maikeTrueYes(userName, userAccount)


# UrlList = ['http://wanxinying.com:80/SubmitInfo/Index?token=on72O0HLstS%2bTrjMnWJuRAXKwhuTKJnjWqtLuQW0yE8pPqn9mCI1hEJzSUrgYMW3cWx%2f70zNL19BT5AMHm5SXl9BOg%2f3hgL0TZhWB7OWgAVXQoHtj07pn5Z7Gwx%2bSJuNYfzN2NypJn9PNZN9zLxBI1iEOH6dORa%2bo8rFTXKWp9c%3d', 'http://wanxinying.com/SubmitInfo/Index?token=on72O0HLstS%2B7EaB16ZG2yC4qAYB0BsB5Rt83b2xdJnfesJPjTwg9k4LHGHeRZq7KvFsL7z3uuuuaYssrPTPCwufvWqKCUCzUeJpG8J6dPxaTadf7XsiVCBcOCUMm1Wlru00RC6PpyNR1oA0SfoHE9sUIPJOKVa2NXidIfcrBIeZg0smEs6qag%3D%3D', 'http://wanxinying.com:80/SubmitInfo/Index?token=on72O0HLstQAtB0pNaoApuK1eUzYaOwO776KUwwbsDiBmRFsvFoWe634vMZVqAqqITdYGO1JiW6dz7RFch4488yHK4boWLxv3iLTSfF3dg97MpzyASGWW84l5%2bB3q8XVW9xemLL7YV0I7y6RxOfb9oJ6em87dpwU0L0XAPsRWQAWbY%2bjN6CGew%3d%3d', 'https://jinshuju.net/f/aM6GUI', 'https://jinshuju.net/f/QU9mq1', 'https://jinshuju.net/f/RnrZwN', 'https://jinshuju.net/f/G7zcWi', 'https://jinshuju.net/f/TZE1NX', 'https://jinshuju.net/f/t7rPus', 'http://yongyushiyan.mikecrm.com/Jn6aZwM', 'http://yongyushiyan.mikecrm.com/I1zwobw', 'http://yongyushiyan.mikecrm.com/3Sa5QkT', 'http://yongyushiyan.mikecrm.com/WC5vJC1', 'http://yongyushiyan.mikecrm.com/LcdzUov', 'http://yongyushiyan.mikecrm.com/0F15NcX', 'http://yongyushiyan.mikecrm.com/0AeFGCX', 'http://yongyushiyan.mikecrm.com/ql3KsfK', 'http://yongyushiyan.mikecrm.com/SIyzPmT']
# SubmitMoney().startRequest('http://yongyushiyan.mikecrm.com/ql3KsfK 测试号 19999999999')
