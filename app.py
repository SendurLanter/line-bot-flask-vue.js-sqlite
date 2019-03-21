from __future__ import unicode_literals
from argparse import ArgumentParser
from flask import Flask, request, abort, jsonify
from linebot import *
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from flask_cors import CORS
import requests
import sqlite3
import json
import sys
import os

app = Flask(__name__)
#CORS問題, 每個route位置都要加,沒這行不行
cors = CORS(app, resources={r"/user": {"origins": "*"},r"/groperson": {"origins": "*"},"/group": {"origins": "*"},r"/menu_id": {"origins": "*"},r"/menu": {"origins": "*"},r"/handler": {"origins": "*"},r"/keyword": {"origins": "*"}})

#channel_secret = 'd504f75f4392eccfa5d5c2999694728f'
channel_secret = '823e0efbee26248f87d96d8a1120372a'
#channel_secret = 'bf2a8bd07bd0f9623240dcd84cfbc0ee'
#channel_access_token = 'mBjRbawKBAS1kRKZaAJhUU4SgJoZshNolWS6zR4zhoAdk+19ZXt0/h5QiSK7hi4zE+jtLhJhbwSvvyy1LAlf/0VnMRJyXUA/9QpHXUt52Wv6DXMIWcUZxSiealvOkEaz52YAhnoGLwnX7ygqMoEHtwdB04t89/1O/w1cDnyilFU='
channel_access_token = 'Q6ucIuRjwEBln3BcZPpBsylGVuwvyVuM9EeA65KcCxHON6CLMSQCKtAErW9Y4LvCtS3o3t68wtsKJtfCJWjvCiAx14GZgfzZNLCMlrDVnjInEaTIxUWY8fsNhE2qgNOUtm/Q4J5vJwnraaDL/34iQwdB04t89/1O/w1cDnyilFU='
#channel_access_token = 'hN769AGqmM0MUHmFF/i+GdbC4FClJsjAEj1FJztDVjjqXiYHopuCQgpaxBezxJMqBFjrtGsQzuMoOdm1GBZFsklDZWQT8yJhNuTytY/oQruVZbdTI9Fhh62cr3QAmI8heH7G5dsn/khQitYqnC+y+QdB04t89/1O/w1cDnyilFU='
#http request
#headers = {"Authorization":"Bearer mBjRbawKBAS1kRKZaAJhUU4SgJoZshNolWS6zR4zhoAdk+19ZXt0/h5QiSK7hi4zE+jtLhJhbwSvvyy1LAlf/0VnMRJyXUA/9QpHXUt52Wv6DXMIWcUZxSiealvOkEaz52YAhnoGLwnX7ygqMoEHtwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
headers = {"Authorization":"Bearer Q6ucIuRjwEBln3BcZPpBsylGVuwvyVuM9EeA65KcCxHON6CLMSQCKtAErW9Y4LvCtS3o3t68wtsKJtfCJWjvCiAx14GZgfzZNLCMlrDVnjInEaTIxUWY8fsNhE2qgNOUtm/Q4J5vJwnraaDL/34iQwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
#line api, 以我line帳號的資訊與line server進行解碼
line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

#連接資料庫
conn = sqlite3.connect('test.db')
c = conn.cursor()

#第一次執行時db創建需要的table
def init():
    c.execute('''CREATE TABLE IF NOT EXISTS kr ( kw varchar , response varchar );''') 
    #menu name 對 menu id
    c.execute('''CREATE TABLE IF NOT EXISTS menuid ( name varchar , id varchar );''') 
    c.execute('''CREATE TABLE IF NOT EXISTS menu_action ( name varchar , buttom varchar , action varchar);''') 
    # keyword 對 menu
    c.execute('''CREATE TABLE IF NOT EXISTS hierachy ( kw varchar , menu varchar);''')
    c.execute('''CREATE TABLE IF NOT EXISTS permission ( name varchar , userid varchar);''')
    #c.execute("INSERT INTO permission (name,userid) VALUES ('%s','%s')"%('user1','Uf4b0e4fcc142d771c55265f6df6ad547'))
    c.execute('''CREATE TABLE IF NOT EXISTS group_person ( person varchar , group_name varchar);''')
    c.execute('''CREATE TABLE IF NOT EXISTS groups ( name varchar);''')
    print('initialized')
    #更新db並離開
    conn.commit()
    conn.close()

#前端發GET到server, 回傳group-person,
@app.route("/groperson",methods=['get'])
def group_to_person():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    data=list()
    for e in c.execute("SELECT * FROM group_person"):
        data.append({'person':e[0],'group_name':e[1]})
    conn.commit()
    conn.close()
    print(jsonify(data))
    return jsonify(data)

#前端發GET到server, 回傳group list,
@app.route("/group",methods=['get'])
def group_name():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    data=list()
    for e in c.execute("SELECT * FROM groups"):
        data.append({'description':e[0]})
    conn.commit()
    conn.close()
    print(jsonify(data))
    return jsonify(data)

#前端發GET到server, 回傳menu name,menu id
@app.route("/menu_id",methods=['get'])
def menu__id():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    data=list()
    for e in c.execute("SELECT * FROM menuid"):
        data.append({'name':e[0],'id':e[1]})
    conn.commit()
    conn.close()
    print(jsonify(data))
    return jsonify(data)

#前端發GET到server, 回傳user name,menu id
@app.route("/user",methods=['get'])
def user__id():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    data=list()
    for e in c.execute("SELECT * FROM permission"):
        data.append({'name':e[0],'id':e[1]})
    conn.commit()
    conn.close()
    print(jsonify(data))
    return jsonify(data)

#前端發GET到server, 回傳menu name,buttom num,action
@app.route("/menu",methods=['get'])
def get_menu():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    data=list()
    for e in c.execute("SELECT * FROM menu_action"):
        data.append({'name':e[0],'buttom':e[1],'action':e[2]})
    conn.commit()
    conn.close()
    print(jsonify(data))
    return jsonify(data)

#前端發GET到server, 回傳keyword,response
@app.route("/keyword",methods=['get'])
def get_kr():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    data = list()
    for e in c.execute("SELECT * FROM kr"):
        data.append({'k':e[0],'r':e[1]})
    conn.commit()
    conn.close()
    print(jsonify(data))
    return jsonify(data)

#處理儲存要做menu的圖片
@app.route("/upload",methods=['POST'])
def receive_file():
    with open('test.jpg', 'wb') as f:
        f.write(request.get_data()[137:-46])

    return 'upload succeed'

#與前端接,處理json request 主要以'source'做請求分類 分別對應到不同的功能
@app.route("/handler",methods=['GET','POST'])
def backend():
    req = request.get_json()
    print(req)
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    #由json中的作來源頁面的分類
    #新增keyword 與對應的response
    if req['source'] == 'text':          
        for d in req['message']:
            print(d)
            c.execute("INSERT INTO kr (kw,response) VALUES ('%s','%s')"%(d['k'],d['r']))

    #creat a menu 製作
    elif req['source'] == 'menu':
        body = {
                "size": {"width": 2500, "height": 1686},
                "selected": "true",
                "name": "Controller",
                "chatBarText": "Controller",
                "areas":[
                    {
                      "bounds": {"x": 400, "y": 400, "width": 800, "height": 800},
                      "action": {"type": req['buttom1']['type'], "text": req['buttom1']['action']}
                    },
                    {
                      "bounds": {"x": 1240, "y": 400, "width": 800, "height": 800},
                      "action": {"type": req['buttom2']['type'], "text": req['buttom2']['action']}
                    },
                    {
                      "bounds": {"x": 2080, "y": 400, "width": 800, "height": 800},
                      "action": {"type": req['buttom3']['type'], "text": req['buttom3']['action']}
                    },
                    {
                      "bounds": {"x": 400, "y": 1240, "width": 800, "height": 800},
                      "action": {"type": req['buttom4']['type'], "text": req['buttom4']['action']}
                    },
                    {
                      "bounds": {"x": 1240, "y": 1240, "width": 800, "height": 800},
                      "action": {"type": req['buttom5']['type'], "uri": req['buttom5']['action']}
                    },
                    {
                      "bounds": {"x": 2080, "y": 1240, "width": 800, "height": 800},
                      "action": {"type": req['buttom6']['type'], "uri": req['buttom6']['action']}
                    }
                ]
              }

        cre = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', headers=headers,data=json.dumps(body).encode('utf-8'))
        id = cre.text[15:-2]
        print(id)
        with open('test.jpg', 'rb') as f:
            line_bot_api.set_rich_menu_image(id, "image/jpeg", f)
        print('menu succeed')
        #存menu id與name
        c.execute("INSERT INTO menuid (name,id) VALUES ('%s','%s')"%(req['name'],id))
        #存buttom對應動作
        for i in range(1,7):
            c.execute("INSERT INTO menu_action (name,buttom,action) VALUES ('%s','%s','%s')"%(req['name'],str(i),req['buttom'+str(i)]['action']))
        print('dataset succeed')

    #製作menu間的hierachy
    elif req['source'] == 'hierachy':
      
        #找main_menu對應的id
        for e in c.execute("SELECT * FROM menuid "):
            #更換主頁
            if e[0] == req['main']:
                cre = requests.request('POST', 'https://api.line.me/v2/bot/user/Uf4b0e4fcc142d771c55265f6df6ad547/richmenu/'+e[1], headers=headers)
        print('start succeed')
        #關鍵字對應menu
        for i in range(1,4):
            print(req['L'+str(i)])
            #第i層
            for l in req['L'+str(i)]:
                #第j個按鈕
                for j in range(6):
                    if l['name'] != 'buttom':
                        if i == 1:
                            thismenu = req['main']
                        else:
                            thismenu = req['L'+str(i-1)][j]['name']
                        #第i層 第j個按鈕對應的 關鍵字與下一個menu 記錄在hierachy 資料庫表中
                        for d in c.execute("SELECT * FROM menu_action WHERE name == ('%s')"%(thismenu)):
                            if d[1] == str(j+1):
                                c.execute("INSERT INTO hierachy (kw , menu) VALUES ('%s','%s')"%(d[2],req['L'+str(i)][j]['name']))

        print('hierachy succeed')

    #負責推播訊息,
    elif req['source'] == 'push':
        for e in c.execute("SELECT * FROM group_person"):
            if e[1]==req['target']['description']:
                print('hit')
                for d in c.execute("SELECT * FROM permission"):
                    if e[0]==d[0]:
                        line_bot_api.push_message(d[1], TextSendMessage(text=req['message']))

    #負責建立group                    
    elif req['source'] == 'group':
        exist=False
        for e in c.execute("SELECT * FROM groups"):
            if e[0]==req['group_name']:
                exist=True
                break
        if not exist:
            c.execute("INSERT INTO groups (name) VALUES ('%s')"%(req['group_name']))
    #負責新增使用者進入group
    elif req['source'] == 'edit':
        exist=False
        for e in c.execute("SELECT * FROM group_person"):
            if e[0]==req['user']:
                exist=True
                break
        if not exist:
            c.execute("INSERT INTO group_person (person,group_name) VALUES ('%s','%s')"%(req['user'],req['group_name']['description']))

    conn.commit()
    conn.close()

    return 'OK'

#主要執行的部分, line server發POST request到callback網址, 在這做解析事件與相對應的動作
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)
    # parse webhook body
    events = parser.parse(body, signature)
    #連接資料庫
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    #事件相對應要做的動作
    #主要是分析語句並搜尋資料庫做回應
    for event in events:
        #message來源的user Id
        userid=str(event.source.user_id)
        exist=False

        #新使用者輸入進資料庫
        for e in c.execute("SELECT * FROM permission"):
            if userid == e[1]:
                exist=True
                break

        if not exist:
            #Uca4cdd54e2f644f09391c45f7b6d6828
            profile = line_bot_api.get_profile(userid)
            print(profile.display_name)
            c.execute("INSERT INTO permission (name,userid) VALUES ('%s','%s')"%(profile.display_name,userid))


        if event.message.text == "貼圖":
            line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=2))
        
        #keyword parse
        for e in c.execute("SELECT * FROM kr"):
            if event.message.text == e[0]:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=e[1]))
        
        #hierachy parse
        for e in c.execute("SELECT * FROM hierachy" ):
            #找關鍵字
            if event.message.text == e[0]:
                #找關鍵字對應的mene id
                for d in c.execute("SELECT * FROM menuid "):
                    #抽換menu
                    if e[1] == d[0]:
                        print('fit')
                        cre = requests.request('POST', 'https://api.line.me/v2/bot/user/'+userid+'/richmenu/'+d[1], headers=headers)
                        print('changed')
    #更新db並離開
    conn.commit()
    conn.close()    
    return 'OK'

#開始執行
if __name__ == "__main__":
    init()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)