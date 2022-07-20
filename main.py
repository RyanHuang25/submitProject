# -*- coding: utf8 -*-
'''
@Author : huangrenwu
@File: main.py
@Time: 2022/7/11 16:10
@Email: leo.r.huang@microcore.tech
@Desc:
'''

import threading
from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import SubmitField
from utils.submitSelenium import SubmitUser,SubmitUserMany,SubmitUserTime,SubmitUserClear

app = Flask(__name__)
app.secret_key = "shawroot"

class Newform(FlaskForm):
    allSubmit = SubmitField('启动所有')
    oneSubmit = SubmitField('启动')
    twoSubmit = SubmitField('启动')
    threeSubmit = SubmitField('启动')
    fourSubmit = SubmitField('启动')
    fiveSubmit = SubmitField('启动')
    sixSubmit = SubmitField('启动')
    sevenSubmit = SubmitField('启动')
    eightSubmit = SubmitField('启动')
    nineSubmit = SubmitField('启动')
    tenSubmit = SubmitField('启动')

class TwoForm(FlaskForm):
    InputSubmit = SubmitField('启动')

def IndexDealOnlyName(data_list):
    infoList = []
    for data in data_list:
        data = data.replace('\r','')
        if data == "":
            continue
        infoList.append(data)
    print(infoList)
    SubmitUser().startRequest(infoList)

def TwoIndexDealName(data_list):
    infoList = []
    for data in data_list:
        data = data.replace('\r','')
        if data == "":
            continue
        infoList.append(data)
    SubmitUserMany().startRequest(infoList)

def ThreeIndexDealName(data_list):
    infoList = []
    for data in data_list:
        data = data.replace('\r', '')
        if data == "":
            continue
        infoList.append(data)
    SubmitUserTime().startRequest(infoList)

def FourIndexDealName(data_list):
    infoList = []
    for data in data_list:
        data = data.replace('\r', '')
        if data == "":
            continue
        infoList.append(data)
    SubmitUserClear().startRequest(infoList)

@app.route('/',methods=['GET','POST'])
def index():
    form = Newform()
    if request.method == "POST":
        if form.oneSubmit.data:
            oneList = request.form.get('one').split('\n')
            IndexDealOnlyName(oneList)
        elif form.twoSubmit.data:
            twoList = request.form.get('two').split('\n')
            IndexDealOnlyName(twoList)
        elif form.threeSubmit.data:
            threeList = request.form.get('three').split('\n')
            IndexDealOnlyName(threeList)
        elif form.fourSubmit.data:
            fourList = request.form.get('four').split('\n')
            IndexDealOnlyName(fourList)
        elif form.fiveSubmit.data:
            fiveList = request.form.get('five').split('\n')
            IndexDealOnlyName(fiveList)
        elif form.sixSubmit.data:
            sixList = request.form.get('six').split('\n')
            IndexDealOnlyName(sixList)
        elif form.sevenSubmit.data:
            sevenList = request.form.get('seven').split('\n')
            IndexDealOnlyName(sevenList)
        elif form.eightSubmit.data:
            eightList = request.form.get('eight').split('\n')
            IndexDealOnlyName(eightList)
        elif form.nineSubmit.data:
            nineList = request.form.get('nine').split('\n')
            IndexDealOnlyName(nineList)
        elif form.tenSubmit.data:
            tenList = request.form.get('ten').split('\n')
            IndexDealOnlyName(tenList)
        elif form.allSubmit.data:
            postItem = {
                "one": request.form.get('one').split('\n'),
                "two": request.form.get('two').split('\n'),
                "three": request.form.get('three').split('\n'),
                "four": request.form.get('four').split('\n'),
                "five": request.form.get('five').split('\n'),
                "six": request.form.get('six').split('\n'),
                "seven": request.form.get('seven').split('\n'),
                "eight": request.form.get('eight').split('\n'),
                "nine": request.form.get('nine').split('\n'),
                "ten": request.form.get('ten').split('\n')
            }
            print(postItem)
            for data in postItem.values():
                if data == ['']:
                    continue
                threading.Thread(target=IndexDealOnlyName,args=(data,)).start()

    return render_template('index.html',form=form)

@app.route('/two',methods=['GET','POST'])
def twoIndex():
    form = TwoForm()
    if request.method == "POST":
        if form.InputSubmit.data:
            inputList = request.form.get('twoText').split('\n')
            TwoIndexDealName(inputList)
    return render_template('two.html',form=form)

@app.route('/three',methods=['GET','POST'])
def threeIndex():
    form = TwoForm()
    if request.method == "POST":
        if form.InputSubmit.data:
            inputList = request.form.get('threeText').split('\n')
            ThreeIndexDealName(inputList)
    return render_template('three.html',form=form)

@app.route('/four',methods=['GET','POST'])
def fourIndex():
    form = TwoForm()
    if request.method == "POST":
        if form.InputSubmit.data:
            inputList = request.form.get('fourText').split('\n')
            FourIndexDealName(inputList)
    return render_template('four.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)


#############测试数据##################
'''
测试号 19999999999 https://jinshuju.net/f/QU9mq1
测试号 19999999999 https://jinshuju.net/f/TZE1NX
测试号 19999999999 http://wanxinying.com:80/SubmitInfo/Index?token=on72O0HLstS%2bTrjMnWJuRAXKwhuTKJnjWqtLuQW0yE8pPqn9mCI1hEJzSUrgYMW3cWx%2f70zNL19BT5AMHm5SXl9BOg%2f3hgL0TZhWB7OWgAVXQoHtj07pn5Z7Gwx%2bSJuNYfzN2NypJn9PNZN9zLxBI1iEOH6dORa%2bo8rFTXKWp9c%3d
测试号 19999999999 http://yongyushiyan.mikecrm.com/WC5vJC1
测试号 19999999999 http://yongyushiyan.mikecrm.com/ql3KsfK
测试号 19999999999 http://yongyushiyan.mikecrm.com/Jn6aZwM
测试号 19999999999 http://yongyushiyan.mikecrm.com/3Sa5QkT
'''