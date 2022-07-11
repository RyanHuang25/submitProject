# -*- coding: utf8 -*-
'''
@Author : huangrenwu
@File: app.py.py
@Time: 2022/7/11 16:10
@Email: leo.r.huang@microcore.tech
@Desc: 
'''

from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import SubmitField
from main.submitTestSelenium import SubmitMoney

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

def startRunOnly(data):
    '''
    启动单个
    :return:
    '''
    SubmitMoney().startRequest(data)

@app.route('/',methods=['GET','POST'])
def index():
    form = Newform()
    if request.method == "POST":
        if form.oneSubmit.data:
            oneData = request.form.get('one')
            SubmitMoney().startRequest(oneData)
        elif form.twoSubmit.data:
            print('点击了第二个按钮')
        elif form.threeSubmit.data:
            print('点击了第二个按钮')
        elif form.fourSubmit.data:
            print('点击了第二个按钮')
        elif form.fiveSubmit.data:
            print('点击了第二个按钮')
        elif form.sixSubmit.data:
            print('点击了第二个按钮')
        elif form.sevenSubmit.data:
            print('点击了第二个按钮')
        elif form.eightSubmit.data:
            print('点击了第二个按钮')
        elif form.nineSubmit.data:
            print('点击了第二个按钮')
        elif form.tenSubmit.data:
            print('点击了第二个按钮')
        elif form.allSubmit.data:
            print('点击了第二个按钮')

    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
