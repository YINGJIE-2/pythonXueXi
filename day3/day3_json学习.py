"""
json 数据和python字典的相互转换
"""

import json

data=[{"name":"长大山","age":11},{"name":"王小二","age":16},{"name":"李小萌","age":81}]

# 列表转换成json
json_str=json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

d = {"name":"周杰伦","addr":"台北"}
json_str2=json.dumps(d,ensure_ascii=False)
print(type(json_str2))
print(json_str2)

# 将json字符串转换成python数据类型
s = '[{"name": "长大山", "age": 11}, {"name": "王小二", "age": 16}, {"name": "李小萌", "age": 81}]'
l = json.loads(s)
print(type(l))
print(l)