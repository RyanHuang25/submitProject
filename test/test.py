# -*- coding: utf8 -*-
'''
@Author: huangrenwu
@File: test.py
@Time: 2022/7/12 00:01
@Email: leo.r.huang@microcore.tech
'''
import random
from selenium import webdriver

def test():

    driver = webdriver.Chrome(executable_path=r"/Users/huangrenwu/Project/submitProject/file/chromedriver")

    driver.get('http://127.0.0.1:5000/')

    UrlList = ['http://wanxinying.com:80/SubmitInfo/Index?token=on72O0HLstS%2bTrjMnWJuRAXKwhuTKJnjWqtLuQW0yE8pPqn9mCI1hEJzSUrgYMW3cWx%2f70zNL19BT5AMHm5SXl9BOg%2f3hgL0TZhWB7OWgAVXQoHtj07pn5Z7Gwx%2bSJuNYfzN2NypJn9PNZN9zLxBI1iEOH6dORa%2bo8rFTXKWp9c%3d', 'http://wanxinying.com/SubmitInfo/Index?token=on72O0HLstS%2B7EaB16ZG2yC4qAYB0BsB5Rt83b2xdJnfesJPjTwg9k4LHGHeRZq7KvFsL7z3uuuuaYssrPTPCwufvWqKCUCzUeJpG8J6dPxaTadf7XsiVCBcOCUMm1Wlru00RC6PpyNR1oA0SfoHE9sUIPJOKVa2NXidIfcrBIeZg0smEs6qag%3D%3D', 'http://wanxinying.com:80/SubmitInfo/Index?token=on72O0HLstQAtB0pNaoApuK1eUzYaOwO776KUwwbsDiBmRFsvFoWe634vMZVqAqqITdYGO1JiW6dz7RFch4488yHK4boWLxv3iLTSfF3dg97MpzyASGWW84l5%2bB3q8XVW9xemLL7YV0I7y6RxOfb9oJ6em87dpwU0L0XAPsRWQAWbY%2bjN6CGew%3d%3d', 'https://jinshuju.net/f/aM6GUI', 'https://jinshuju.net/f/QU9mq1', 'https://jinshuju.net/f/RnrZwN', 'https://jinshuju.net/f/G7zcWi', 'https://jinshuju.net/f/TZE1NX', 'https://jinshuju.net/f/t7rPus', 'http://yongyushiyan.mikecrm.com/Jn6aZwM', 'http://yongyushiyan.mikecrm.com/I1zwobw', 'http://yongyushiyan.mikecrm.com/3Sa5QkT', 'http://yongyushiyan.mikecrm.com/WC5vJC1', 'http://yongyushiyan.mikecrm.com/LcdzUov', 'http://yongyushiyan.mikecrm.com/0F15NcX', 'http://yongyushiyan.mikecrm.com/0AeFGCX', 'http://yongyushiyan.mikecrm.com/ql3KsfK', 'http://yongyushiyan.mikecrm.com/SIyzPmT']
    inputList = ['one','two','three','four','five','six','seven','eight','nine','ten']

    for i in inputList:
        driver.find_element_by_xpath(f"//input[@name='{i}']").send_keys(f"{random.choice(UrlList)} 测试号 19999999999")

    driver.find_element_by_id('allSubmit').click()
# driver.quit()
test()