"""
文件读取类
"""
import json

from data_define import Record

# 抽象类规定必须完成的工作
class FileReader:

    def read_data(self) -> list[Record]:
        """读取文件的数据，读到的每一条数据都转换为Recore对象，将他们封装到list内返回"""

    pass


class TextFileReader(FileReader):
    def __init__(self, path, ):
        self.path = path  # 定义成员变量得到文件路径

    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        f = open(self.path, 'r', encoding='utf-8')
        for line in f.readlines():
            line = line.strip()  # 删除前后空格和回车
            data_list = line.split(',')  # 以,号分割字符串
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self):
        record_list: list[Record] = []
        f = open(self.path, 'r', encoding='utf-8')
        for line in f.readlines():
            data_dict = json.loads(line)
            record=Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)
        f.close()
        return record_list



