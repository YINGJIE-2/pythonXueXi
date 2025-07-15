from day6.综合案例.data_define import Record
from day6.综合案例.file_define import TextFileReader, JsonFileReader
from pymysql import Connection

text_file_reader = TextFileReader("2011年1月销售数据.txt")
json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的list存到一个list里面

all_list: list[Record] = jan_data + feb_data

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    passwd="123456",
    autocommit=True
)

# 获取游标对象

cursor = conn.cursor()
conn.select_db("py_sql")

for record in all_list:
    sql = (f"insert into orders(order_date,order_id,money,province)"
           f" values ('{record.date}','{record.order_id}','{record.money}','{record.province}')")
    cursor.execute(sql)

conn.close()

