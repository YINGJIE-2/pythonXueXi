my_dict= {"小米13": 1299, "华为p90": 1399, "苹果13": 1499}
print(my_dict)
#添加元素

my_dict["华为33"]=999
print(my_dict)

#更新元素

my_dict["小米13"]=11111
print(my_dict)

#删除元素

scort=my_dict.pop("小米13")
print(my_dict)

#清空字典

# my_dict.clear()
# print(my_dict)

#获取全部key

keys=my_dict.keys()
print(keys)

#字典便利
#方法1
for key in keys:
    print(my_dict[key])

#方法2
for key in my_dict:
    print(my_dict[key])