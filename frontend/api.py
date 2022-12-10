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

# layer1 phone name api
@app.route('/api/phonename')
@cross_origin()
def getRowOneName():
    connection = connect_db()
    cur = connection.cursor()
    getName = "SELECT name FROM tbl_product WHERE brand_id = 1"
    cur.execute(getName)
    name = cur.fetchall()
    jsonResp = {
        'ph1': name[0],
        'ph2': name[1],
        'ph3': name[2],
        'ph4': name[3],
        'ph5': name[4],
        'ph6': name[5]
    }
    return jsonify(jsonResp)

# layer1 popular apple product api
@app.route('/api/applepop')
@cross_origin()
def getRow1Product():
    connection = connect_db()
    cur = connection.cursor()
    getProduct = "SELECT product_id, name FROM tbl_product WHERE brand_id = 1"
    cur.execute(getProduct)
    product = cur.fetchall()
    jsonResp = []
    for i in range(6):
        product_content = {}
        product_content['product_id'] = product[i][0]
        product_content['name'] = product[i][1]
        jsonResp.append(product_content)
    
    return jsonify(jsonResp)

# layer1 popular google product api
@app.route('/api/googlepop')
@cross_origin()
def getRow2Product():
    connection = connect_db()
    cur = connection.cursor()
    getProduct = "SELECT product_id, name FROM tbl_product WHERE brand_id = 3"
    cur.execute(getProduct)
    product = cur.fetchall()
    jsonResp = []
    for i in range(6):
        product_content = {}
        product_content['product_id'] = product[i][0]
        product_content['name'] = product[i][1]
        jsonResp.append(product_content)
    
    return jsonify(jsonResp)

# layer2 popular apple product api
@app.route('/api/appleproduct')
@cross_origin()
def getAppleProduct():
    connection = connect_db()
    cur = connection.cursor()
    getProduct = "SELECT product_id, name FROM tbl_product WHERE brand_id = 1"
    cur.execute(getProduct)
    product = cur.fetchall()
    jsonResp = []
    for i in range(6):
        product_content = {}
        product_content['product_id'] = product[i][0]
        product_content['name'] = product[i][1]
        jsonResp.append(product_content)
    
    return jsonify(jsonResp)

# iphoneSE3
# layer3 post api
@app.route('/api/iphonese3/phonepost')
@cross_origin()
def getPhonePost1():
    connection = connect_db()
    cur = connection.cursor()
    getPost = "SELECT post_id, source_id, title, link, date FROM tbl_post WHERE product_id = 1 ORDER BY date DESC"
    cur.execute(getPost)
    post = cur.fetchall()
    jsonResp = []
    for i in range(len(post)):
        post_details = {}
        post_details['id'] = post[i][0]
        post_details['src_id'] = post[i][1]
        post_details['title'] = post[i][2]
        post_details['link'] = post[i][3]
        post_details['date'] = post[i][4]
        jsonResp.append(post_details)
    
    return jsonify(jsonResp)

# layer3 feature budget api
@app.route('/api/iphonese3/feature/budget')
@cross_origin()
def getFtBudget1():
    connection = connect_db()
    cur = connection.cursor()
    getFtBudget = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 1 AND label_id = 1"
    cur.execute(getFtBudget)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature wafer api
@app.route('/api/iphonese3/feature/wafer')
@cross_origin()
def getFtWafer1():
    connection = connect_db()
    cur = connection.cursor()
    getFtWafer = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 1 AND label_id = 2"
    cur.execute(getFtWafer)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature screen api
@app.route('/api/iphonese3/feature/screen')
@cross_origin()
def getFtScreen1():
    connection = connect_db()
    cur = connection.cursor()
    getFtScreen = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 1 AND label_id = 3"
    cur.execute(getFtScreen)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature battery api
@app.route('/api/iphonese3/feature/battery')
@cross_origin()
def getFtBattery1():
    connection = connect_db()
    cur = connection.cursor()
    getFtBattery = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 1 AND label_id = 4"
    cur.execute(getFtBattery)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature lens api
@app.route('/api/iphonese3/feature/lens')
@cross_origin()
def getFtLens1():
    connection = connect_db()
    cur = connection.cursor()
    getFtLens = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 1 AND label_id = 5"
    cur.execute(getFtLens)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature capacity api
@app.route('/api/iphonese3/feature/capacity')
@cross_origin()
def getFtCapacity1():
    connection = connect_db()
    cur = connection.cursor()
    getFtCapacity = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 1 AND label_id = 6"
    cur.execute(getFtCapacity)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# iphone13 mini
# layer3 post api
@app.route('/api/iphone13mini/phonepost')
@cross_origin()
def getPhonePost2():
    connection = connect_db()
    cur = connection.cursor()
    getPost = "SELECT post_id, source_id, title, link, date FROM tbl_post WHERE product_id = 2 ORDER BY date DESC"
    cur.execute(getPost)
    post = cur.fetchall()
    jsonResp = []
    for i in range(len(post)):
        post_details = {}
        post_details['id'] = post[i][0]
        post_details['src_id'] = post[i][1]
        post_details['title'] = post[i][2]
        post_details['link'] = post[i][3]
        post_details['date'] = post[i][4]
        jsonResp.append(post_details)
    
    return jsonify(jsonResp)

# layer3 feature budget api
@app.route('/api/iphone13mini/feature/budget')
@cross_origin()
def getFtBudget2():
    connection = connect_db()
    cur = connection.cursor()
    getFtBudget = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 2 AND label_id = 1"
    cur.execute(getFtBudget)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature wafer api
@app.route('/api/iphone13mini/feature/wafer')
@cross_origin()
def getFtWafer2():
    connection = connect_db()
    cur = connection.cursor()
    getFtWafer = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 2 AND label_id = 2"
    cur.execute(getFtWafer)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature screen api
@app.route('/api/iphone13mini/feature/screen')
@cross_origin()
def getFtScreen2():
    connection = connect_db()
    cur = connection.cursor()
    getFtScreen = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 2 AND label_id = 3"
    cur.execute(getFtScreen)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature battery api
@app.route('/api/iphone13mini/feature/battery')
@cross_origin()
def getFtBattery2():
    connection = connect_db()
    cur = connection.cursor()
    getFtBattery = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 2 AND label_id = 4"
    cur.execute(getFtBattery)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature lens api
@app.route('/api/iphone13mini/feature/lens')
@cross_origin()
def getFtLens2():
    connection = connect_db()
    cur = connection.cursor()
    getFtLens = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 2 AND label_id = 5"
    cur.execute(getFtLens)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature capacity api
@app.route('/api/iphone13mini/feature/capacity')
@cross_origin()
def getFtCapacity2():
    connection = connect_db()
    cur = connection.cursor()
    getFtCapacity = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 2 AND label_id = 6"
    cur.execute(getFtCapacity)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# iphone13
# layer3 post api
@app.route('/api/iphone13/phonepost')
@cross_origin()
def getPhonePost3():
    connection = connect_db()
    cur = connection.cursor()
    getPost = "SELECT post_id, source_id, title, link, date FROM tbl_post WHERE product_id = 3 ORDER BY date DESC"
    cur.execute(getPost)
    post = cur.fetchall()
    jsonResp = []
    for i in range(len(post)):
        post_details = {}
        post_details['id'] = post[i][0]
        post_details['src_id'] = post[i][1]
        post_details['title'] = post[i][2]
        post_details['link'] = post[i][3]
        post_details['date'] = post[i][4]
        jsonResp.append(post_details)
    
    return jsonify(jsonResp)

# layer3 feature budget api
@app.route('/api/iphone13/feature/budget')
@cross_origin()
def getFtBudget3():
    connection = connect_db()
    cur = connection.cursor()
    getFtBudget = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 3 AND label_id = 1"
    cur.execute(getFtBudget)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature wafer api
@app.route('/api/iphone13/feature/wafer')
@cross_origin()
def getFtWafer3():
    connection = connect_db()
    cur = connection.cursor()
    getFtWafer = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 3 AND label_id = 2"
    cur.execute(getFtWafer)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature screen api
@app.route('/api/iphone13/feature/screen')
@cross_origin()
def getFtScreen3():
    connection = connect_db()
    cur = connection.cursor()
    getFtScreen = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 3 AND label_id = 3"
    cur.execute(getFtScreen)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature battery api
@app.route('/api/iphone13/feature/battery')
@cross_origin()
def getFtBattery3():
    connection = connect_db()
    cur = connection.cursor()
    getFtBattery = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 3 AND label_id = 4"
    cur.execute(getFtBattery)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature lens api
@app.route('/api/iphone13/feature/lens')
@cross_origin()
def getFtLens3():
    connection = connect_db()
    cur = connection.cursor()
    getFtLens = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 3 AND label_id = 5"
    cur.execute(getFtLens)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature capacity api
@app.route('/api/iphone13/feature/capacity')
@cross_origin()
def getFtCapacity3():
    connection = connect_db()
    cur = connection.cursor()
    getFtCapacity = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 3 AND label_id = 6"
    cur.execute(getFtCapacity)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# iphone13 pro
# layer3 post api
@app.route('/api/iphone13pro/phonepost')
@cross_origin()
def getPhonePost4():
    connection = connect_db()
    cur = connection.cursor()
    getPost = "SELECT post_id, source_id, title, link, date FROM tbl_post WHERE product_id = 4 ORDER BY date DESC"
    cur.execute(getPost)
    post = cur.fetchall()
    jsonResp = []
    for i in range(len(post)):
        post_details = {}
        post_details['id'] = post[i][0]
        post_details['src_id'] = post[i][1]
        post_details['title'] = post[i][2]
        post_details['link'] = post[i][3]
        post_details['date'] = post[i][4]
        jsonResp.append(post_details)
    
    return jsonify(jsonResp)

# layer3 feature budget api
@app.route('/api/iphone13pro/feature/budget')
@cross_origin()
def getFtBudget4():
    connection = connect_db()
    cur = connection.cursor()
    getFtBudget = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 4 AND label_id = 1"
    cur.execute(getFtBudget)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature wafer api
@app.route('/api/iphone13pro/feature/wafer')
@cross_origin()
def getFtWafer4():
    connection = connect_db()
    cur = connection.cursor()
    getFtWafer = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 4 AND label_id = 2"
    cur.execute(getFtWafer)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature screen api
@app.route('/api/iphone13pro/feature/screen')
@cross_origin()
def getFtScreen4():
    connection = connect_db()
    cur = connection.cursor()
    getFtScreen = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 4 AND label_id = 3"
    cur.execute(getFtScreen)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature battery api
@app.route('/api/iphone13pro/feature/battery')
@cross_origin()
def getFtBattery4():
    connection = connect_db()
    cur = connection.cursor()
    getFtBattery = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 4 AND label_id = 4"
    cur.execute(getFtBattery)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature lens api
@app.route('/api/iphone13pro/feature/lens')
@cross_origin()
def getFtLens4():
    connection = connect_db()
    cur = connection.cursor()
    getFtLens = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 4 AND label_id = 5"
    cur.execute(getFtLens)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature capacity api
@app.route('/api/iphone13pro/feature/capacity')
@cross_origin()
def getFtCapacity4():
    connection = connect_db()
    cur = connection.cursor()
    getFtCapacity = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 4 AND label_id = 6"
    cur.execute(getFtCapacity)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# iphone13 pro max
# layer3 post api
@app.route('/api/iphone13promax/phonepost')
@cross_origin()
def getPhonePost5():
    connection = connect_db()
    cur = connection.cursor()
    getPost = "SELECT post_id, source_id, title, link, date FROM tbl_post WHERE product_id = 5 ORDER BY date DESC"
    cur.execute(getPost)
    post = cur.fetchall()
    jsonResp = []
    for i in range(len(post)):
        post_details = {}
        post_details['id'] = post[i][0]
        post_details['src_id'] = post[i][1]
        post_details['title'] = post[i][2]
        post_details['link'] = post[i][3]
        post_details['date'] = post[i][4]
        jsonResp.append(post_details)
    
    return jsonify(jsonResp)

# layer3 feature budget api
@app.route('/api/iphone13promax/feature/budget')
@cross_origin()
def getFtBudget5():
    connection = connect_db()
    cur = connection.cursor()
    getFtBudget = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 5 AND label_id = 1"
    cur.execute(getFtBudget)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature wafer api
@app.route('/api/iphone13promax/feature/wafer')
@cross_origin()
def getFtWafer5():
    connection = connect_db()
    cur = connection.cursor()
    getFtWafer = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 5 AND label_id = 2"
    cur.execute(getFtWafer)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature screen api
@app.route('/api/iphone13promax/feature/screen')
@cross_origin()
def getFtScreen5():
    connection = connect_db()
    cur = connection.cursor()
    getFtScreen = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 5 AND label_id = 3"
    cur.execute(getFtScreen)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature battery api
@app.route('/api/iphone13promax/feature/battery')
@cross_origin()
def getFtBattery5():
    connection = connect_db()
    cur = connection.cursor()
    getFtBattery = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 5 AND label_id = 4"
    cur.execute(getFtBattery)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature lens api
@app.route('/api/iphone13promax/feature/lens')
@cross_origin()
def getFtLens5():
    connection = connect_db()
    cur = connection.cursor()
    getFtLens = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 5 AND label_id = 5"
    cur.execute(getFtLens)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature capacity api
@app.route('/api/iphone13promax/feature/capacity')
@cross_origin()
def getFtCapacity5():
    connection = connect_db()
    cur = connection.cursor()
    getFtCapacity = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 5 AND label_id = 6"
    cur.execute(getFtCapacity)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# iphone12 mini
# layer3 post api
@app.route('/api/iphone12mini/phonepost')
@cross_origin()
def getPhonePost6():
    connection = connect_db()
    cur = connection.cursor()
    getPost = "SELECT post_id, source_id, title, link, date FROM tbl_post WHERE product_id = 6 ORDER BY date DESC"
    cur.execute(getPost)
    post = cur.fetchall()
    jsonResp = []
    for i in range(len(post)):
        post_details = {}
        post_details['id'] = post[i][0]
        post_details['src_id'] = post[i][1]
        post_details['title'] = post[i][2]
        post_details['link'] = post[i][3]
        post_details['date'] = post[i][4]
        jsonResp.append(post_details)
    
    return jsonify(jsonResp)

# layer3 feature budget api
@app.route('/api/iphone12mini/feature/budget')
@cross_origin()
def getFtBudget6():
    connection = connect_db()
    cur = connection.cursor()
    getFtBudget = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 6 AND label_id = 1"
    cur.execute(getFtBudget)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature wafer api
@app.route('/api/iphone12mini/feature/wafer')
@cross_origin()
def getFtWafer6():
    connection = connect_db()
    cur = connection.cursor()
    getFtWafer = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 6 AND label_id = 2"
    cur.execute(getFtWafer)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature screen api
@app.route('/api/iphone12mini/feature/screen')
@cross_origin()
def getFtScreen6():
    connection = connect_db()
    cur = connection.cursor()
    getFtScreen = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 6 AND label_id = 3"
    cur.execute(getFtScreen)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature battery api
@app.route('/api/iphone12mini/feature/battery')
@cross_origin()
def getFtBattery6():
    connection = connect_db()
    cur = connection.cursor()
    getFtBattery = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 6 AND label_id = 4"
    cur.execute(getFtBattery)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature lens api
@app.route('/api/iphone12mini/feature/lens')
@cross_origin()
def getFtLens6():
    connection = connect_db()
    cur = connection.cursor()
    getFtLens = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 6 AND label_id = 5"
    cur.execute(getFtLens)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

# layer3 feature capacity api
@app.route('/api/iphone12mini/feature/capacity')
@cross_origin()
def getFtCapacity6():
    connection = connect_db()
    cur = connection.cursor()
    getFtCapacity = "SELECT content, label_id FROM tbl_label_detail WHERE product_id = 6 AND label_id = 6"
    cur.execute(getFtCapacity)
    feature = cur.fetchall()
    jsonResp = []
    for i in range(len(feature)):
        feature_details = {}
        feature_details['content'] = feature[i][0]
        feature_details['label_id'] = feature[i][1]
        
        jsonResp.append(feature_details)
    
    return jsonify(jsonResp)

if __name__ == '__main__':
    app.run(debug=False)