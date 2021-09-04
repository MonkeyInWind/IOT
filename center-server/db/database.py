import pymysql;
from uuid import uuid4;
import time;

db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "111111",
    database = "iot"
);
cursor = db.cursor();

def executeInsert(sql):
    try:
       # 执行sql语句
       cursor.execute(sql);
       # 提交到数据库执行
       db.commit();
    except:
       # 如果发生错误则回滚
       db.rollback();

def excuteSelectAll(sql):
    try:
        cursor.execute(sql);
        result = cursor.fetchall();
        return result;
    except Exception as err:
        print(err);
        print("fetch data error", sql);

def insertHT(data):
    t = int(round(time.time() * 1000));
    uuid = uuid4();
    macAddress = data["macAddress"];
    temp = data["temp"];
    humi = data["humi"];
    sql = f"INSERT INTO ht(id, macAddress, temp, humi, timestamp) VALUES ('{uuid}', '{macAddress}', '{temp}', '{humi}', {t})";
    executeInsert(sql);

def selectDevices(type):
    sql = f"select * from devices where type = '{type}'";
    return excuteSelectAll(sql);

def selectHT(start, end):
    sql = f"select * from ht where timestamp >= '{start}' and timestamp <= '{end}'";
    return excuteSelectAll(sql);