import pymysql
import time
import json


host = 'localhost' # 127.0.0.1
port = 3306
user = 'root'
passwd = '8174root'
db = 'TESTDB'
charset = 'utf8mb4'

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)

cursor = conn.cursor()


sql = """
INSERT INTO Staff (ID, Name, DeptId, Age, Gender, Salary, recordDt)
VALUES ('001', 'Mike', '002', 45, 'M', 60000, '2020-04-24 14:59:57');
"""

cursor.execute(sql)
conn.commit()
sql = """
SELECT * FROM Staff;
"""
cursor.execute(sql)

cursor.fetchall()

t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# print(t)


sql = """
INSERT INTO Staff (ID, Name, DeptId, Age, Gender, Salary, recordDt)
VALUES ('002', 'Mike', '002', 45, 'M', 60000, '%s');
"""%(t)


cursor.execute(sql)
conn.commit()

sql = """DELETE FROM Staff;"""
cursor.execute(sql)
conn.commit()


path = 'staff.json'
with open(path, 'r', encoding='utf-8') as f:
    tmpStr = f.read()
    data = json.loads(tmpStr)
data