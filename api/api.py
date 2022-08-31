from flask import Flask, jsonify
from flask_cors import cross_origin
import pymysql
import json
import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# 取得mysql的資料(.env裡的內容)
mysql_host = os.getenv("DB_HOST")
mysql_port = os.getenv("DB_PORT")
mysql_dbname = os.getenv("DB_DATABASE")
mysql_user = os.getenv("DB_USERNAME")
mysql_password = os.getenv("DB_PASSWORD")

connection = None
CONNECTION_TIMEOUT = 5000

print(mysql_host)
print(mysql_port)
print(mysql_dbname)
print(mysql_user)

# 連接資料庫
def connect_db():
    connection = pymysql.connect(host=mysql_host, user=mysql_user, port=int(mysql_port), password=mysql_password, database=mysql_dbname, connect_timeout=CONNECTION_TIMEOUT)
    print("connected to db")
    return connection

def get_cursor(connection): 
    connection.ping(reconnect=True)
    return connection.cursor()

app = Flask(__name__)

# 設定路由存放資料庫抓下來的json
@app.route('/api/phonename')
@cross_origin()
def getPhoneName():
    connection = connect_db()
    cur = connection.cursor()
    getPhoneName = "SELECT name FROM tbl_product WHERE product_id BETWEEN 1 AND 6" # 從資料庫頭開始抓
    # getPhone = "SELECT phonename FROM product ORDER BY id DESC" # 從資料庫尾開始抓
    cur.execute(getPhoneName)
    phonename = cur.fetchall()
    jsonResp = {
        'ph1': phonename[0],
        'ph2': phonename[1],
        'ph3': phonename[2],
        'ph4': phonename[3],
        'ph5': phonename[4],
        'ph6': phonename[5]
    }
    return jsonify(jsonResp)

@app.route('/api/phonepost')
@cross_origin()
def getPhonePost():
    connection = connect_db()
    cur = connection.cursor()
    getPost = "SELECT post_id, title, link, date FROM tbl_post"
    cur.execute(getPost)
    post = cur.fetchall()
    jsonResp = []
    for i in range(20):
        post_details = {}
        post_details['id'] = post[i][0]
        post_details['title'] = post[i][1]
        post_details['link'] = post[i][2]
        post_details['date'] = post[i][3]
        jsonResp.append(post_details)
    
    return jsonify(jsonResp)
'''
@app.route('/api/phonepost')
@cross_origin()
def getPhonePost():
    connection = connect_db()
    cur = connection.cursor()
    getPost = "SELECT title, link, date FROM tbl_post WHERE product_id BETWEEN 1 AND 10"
    cur.execute(getPost)
    post = cur.fetchall()
    jsonResp = {
        'p1':{ 'title': post[0][0], 'link': post[0][1], 'date': post[0][2] },
        'p2':{ 'title': post[1][0], 'link': post[1][1], 'date': post[1][2] },
        'p3':{ 'title': post[2][0], 'link': post[2][1], 'date': post[2][2] },
        'p4':{ 'title': post[3][0], 'link': post[3][1], 'date': post[3][2] }
    }
    return jsonify(jsonResp)
'''

if __name__ == '__main__':
    app.run(debug=False)