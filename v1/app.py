# -*- coding: utf8 -*-
'''
@Author : huangrenwu
@File: app.py.py
@Time: 2022/7/11 16:10
@Email: leo.r.huang@microcore.tech
@Desc: 
'''
import threading
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
            print(request.form.get('one'))
            oneData = request.form.get('one')
            SubmitMoney().startRequest(oneData)
        elif form.twoSubmit.data:
            twoData = request.form.get('two')
            SubmitMoney().startRequest(twoData)
        elif form.threeSubmit.data:
            threeData = request.form.get('three')
            SubmitMoney().startRequest(threeData)
        elif form.fourSubmit.data:
            fourData = request.form.get('four')
            SubmitMoney().startRequest(fourData)
        elif form.fiveSubmit.data:
            fiveData = request.form.get('five')
            SubmitMoney().startRequest(fiveData)
        elif form.sixSubmit.data:
            sixData = request.form.get('six')
            SubmitMoney().startRequest(sixData)
        elif form.sevenSubmit.data:
            sevenData = request.form.get('seven')
            SubmitMoney().startRequest(sevenData)
        elif form.eightSubmit.data:
            eightData = request.form.get('eight')
            SubmitMoney().startRequest(eightData)
        elif form.nineSubmit.data:
            nineData = request.form.get('nine')
            SubmitMoney().startRequest(nineData)
        elif form.tenSubmit.data:
            tenData = request.form.get('ten')
            SubmitMoney().startRequest(tenData)
        elif form.allSubmit.data:
            postItem = {
                "one": request.form.get('one'),
                "two": request.form.get('two'),
                "three": request.form.get('three'),
                "four": request.form.get('four'),
                "five": request.form.get('five'),
                "six": request.form.get('six'),
                "seven": request.form.get('seven'),
                "eight": request.form.get('eight'),
                "nine": request.form.get('nine'),
                "ten": request.form.get('ten'),
            }
        #     for data in postItem.values():
        #         threading.Thread(target=startRunOnly,args=(data,)).start()

    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
