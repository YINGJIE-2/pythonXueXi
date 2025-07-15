from pymysql import Connection
# python 通过pymysql连接mysql数据库
# 获取mysql连接对象
conn = Connection(
    host='localhost',  # 主机名
    port=3306,
    user='root',
    password='123456'
)

# 获取游标对象
cursor = conn.cursor()
# 执行sql
# cursor.execute("CREATE DATABASE IF NOT EXISTS test_python")
# 选择数据库
conn.select_db('jdbc')
# 创建一个表
# cursor.execute("CREATE TABLE test_pymysql(id INT);")

# 查询性语句

cursor.execute("SELECT * FROM student")
resort = cursor.fetchall()
for r in resort:
    print(r)
# 关闭连接
conn.close()
