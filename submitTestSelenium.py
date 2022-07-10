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

import random,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Submit:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'/Users/huangrenwu/Project/submitProject/chromedriver')
        self.driver.maximize_window()
        self.startRequest()

    def startRequest(self):
        # if url in chuangxin['chuangxinFalse']:
        #     print(f'正在打开创鑫链接：{url}')
        # inputDate = input()
        # data_list = inputDate.split(' ')
        # url = data_list[0]
        # userName = data_list[1]
        # userAccount = data_list[2]
        url = 'https://www.baidu.com/'
        self.driver.get(url)
        time.sleep(2)
        js = "window.open('https://baijiahao.baidu.com/s?id=1737929859012797966')"
        self.driver.execute_script(js)
        # handles = self.driver.window_handles
        # print(handles)
        # self.driver.switch_to_window(handles[2])

    def chuangxin(self,userName,userAccount):
        userNameInput = self.driver.find_element_by_id('name')
        userNameInput.send_keys(userName)
        userAccountInput = self.driver.find_element_by_id('telphone')
        userAccountInput.send_keys(userAccount)
        self.driver.find_element_by_id('regBtn').click()
        time.sleep(2)
        try:
            # 判断网页是否提交成功
            Wait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "xxx")))
        except:
            self.chuangxin(userName,userAccount)

if __name__ == '__main__':
    Submit()
