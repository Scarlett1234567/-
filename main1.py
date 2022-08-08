import datetime
import random
import time

import pymysql
from function import function
writeInSQL = []
conn = pymysql.connect(host='localhost',
                        user='',# 数据库名
                        password='',# 数据库密码
                        db='autoinput',
                        charset='utf8')

cursor = conn.cursor()

sql = "select * from athome"

try:
    # 执行SQL语句
    cursor.execute(sql)
    result = cursor.fetchone()
    f = open("log_AUG.txt", "a")
    f.write("TABLE = ATHOME" + " START TIME = " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
    f.close()
    while result is not None:
        if result[11] == 1:
            randomInt = random.randint(60, 120)# 相邻两个填报的时间间隔随机数
            time.sleep(randomInt)
            function(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9])
            f = open("log_AUG.txt", "a")
            f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Interval = " + str(randomInt) + " " + result[0] + " " + result[10] + "\n")
            f.close()
        result = cursor.fetchone()

except:
    print("Error: unable to fetch data")

f = open("log_AUG.txt", "a")# 写日志
f.write("\n")
f.close()
