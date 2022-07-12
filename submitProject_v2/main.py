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
from utils.submitSelenium import SubmitUser

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

def IndexDealOnlyName(data_list):
    infoList = []
    for data in data_list:
        data = data.replace('\r','')
        if data == "":
            continue
        infoList.append(data)
    SubmitUser().startRequest(infoList)


@app.route('/',methods=['GET','POST'])
def index():
    form = Newform()
    if request.method == "POST":
        if form.oneSubmit.data:
            oneList = request.form.get('one').split('\n')
            IndexDealOnlyName(oneList)

    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)