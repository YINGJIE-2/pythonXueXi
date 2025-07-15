from pymysql import Connection

# python 通过pymysql连接mysql数据库   # 插入行为需要确认
# 获取mysql连接对象
conn = Connection(
    host='localhost',  # 主机名
    port=3306,
    user='root',
    password='123456',
    autocommit=True  # 自动提交
)

# 获取游标对象
cursor = conn.cursor()
# 执行sql
conn.select_db("test_python")

cursor.execute("INSERT INTO test_pymysql VALUES (01,'BJ',18)")

conn.commit()  # 手动提交
conn.close()
