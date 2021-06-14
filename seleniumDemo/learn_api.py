# 导入pymysql模块
import pymysql
import os

DB_HOST = 'rm-bp1h64i0euj6x99d9po.mysql.rds.aliyuncs.com'
DB_USERNAME = 'root'
DB_PASSWORD = 'Rkz2C7nM2@#$%^&*()xsowswcDeCr'
DB_DATABASE = 'qsc_grows_v2'

# 连接database
try:
    conn = pymysql.connect(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)
    print('数据库连接成功')
except pymysql.Error as e:
    print('数据库连接失败'+str(e))

# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()

# 定义要执行的SQL语句
sql = "SELECT * FROM grows_adtask_mapping WHERE adslot_id = 201"

# 执行SQL语句
cursor.execute(sql)
data = cursor.fetchall()  # 查询所有数据
print('数据库数据', data)

formatData = []
for i in data:
    text = {'id': i[0], 'name': i[1], 'business_id': i[2], 'business_name': i[3]}
    print(text)
    formatData.append(text)

# 关闭光标对象
cursor.close()

# 关闭数据库连接
conn.close()
