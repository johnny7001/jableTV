import base64
import json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import column
import os
from dotenv import load_dotenv
load_dotenv()

db_host = os.getenv("db_host")
db_user = os.getenv("db_user")
db_password = os.getenv('db_password')
db_name = os.getenv('db_name')
db_charset = os.getenv('db_charset')
db_port = 8889

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
db = SQLAlchemy(app)


@app.route('/')
def home():
    # 地點
    return ('this is jabletvAPI')


@app.route('/videos/<dir_name>', methods=['POST'])
# https://127.0.0.1/videos/fsdss-421/
# 接收番號搜尋影片內容
def index_by_number(dir_name):
    data_dict = {}
    try:
        # 影片內容
        sql = f"SELECT * FROM shane.jable01_tv where dir_name like '{dir_name}';"
        query_data = db.engine.execute(sql)
        result = query_data.fetchone()
        if result != None:
            # print(result['id'])
            # 列出欄位名稱
            sql = "SELECT COLUMN_NAME \
                FROM INFORMATION_SCHEMA.COLUMNS \
                    WHERE TABLE_SCHEMA = 'shane'AND TABLE_NAME = 'jable01_tv';"
            query_data = db.engine.execute(sql)
            columns = query_data.fetchall()  # columns type = list

            # 將欄位名稱及內容配對成字典
            for c in columns:
                c_name = c[0]
                data_dict[f'{c_name}'] = result[f'{c_name}']
            return (data_dict)
        else:
            content = '番號輸入錯誤或影片資訊不存在'
            print(content)
            return (content)
    except:
        return ('執行失敗')

# 輸入video status 查詢影片資訊


@app.route('/status/<status>', methods=['POST'])
def index_by_status(status):
    url_list = []
    try:
        sql = f"SELECT `url` FROM shane.jable01_tv where `status` = '{status}';"
        query_data = db.engine.execute(sql)
        result = query_data.fetchall()
        if result != None:
            for u in result:
                url_list.append(u['url'])
            return (str(url_list))
        return ('查詢不到此狀態')
    except:
        return ('執行失敗')

# 輸入id, 獲得影片番號


@app.route('/id_number/<video_number>', methods=['POST'])
def index_by_id(video_number):
    try:
        sql = f"SELECT `dir_name` FROM shane.jable01_tv where `id` = '{video_number}';"
        query_data = db.engine.execute(sql)
        result = query_data.fetchone()
        if result != None:
            video_number = result['dir_name']
            return (str(video_number))
        return ('查詢不到此id的資料')
    except:
        return ('執行失敗')

# 確認番號是否存在於資料庫內


@app.route('/check_number/<video_number>', methods=['POST'])
def check_number_exists(video_number):
    try:
        sql = f"select dir_name from shane.jable01_tv where dir_name = '{video_number}';"
        query_data = db.engine.execute(sql)
        result = query_data.fetchone()
        anw = result[0] if result != None else '不存在於資料庫'
        return (anw)
    except:
        return ('執行失敗')

# 查詢目前影片狀態的數量, status = 0 (尚未下載), = 1 (下載中), = 2 (完成下載)


@app.route('/check_videos/<status>', methods=['POST'])
def check_videos_status(status):
    try:
        sql = f"select count(id) from shane.jable01_tv where status = '{status}';"
        query_data = db.engine.execute(sql)
        result = query_data.fetchone()
        anw = result[0]
        return (str(anw))
    except:
        return ('執行失敗')


app.run(host='0.0.0.0', port=3123, debug=True)
