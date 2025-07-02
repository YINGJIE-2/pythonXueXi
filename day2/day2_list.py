name=["heima","Python","Java",123,True]
print(name,  type(name))

"""
列表方法使用list_name.
"""
#查找下标
index=name.index("Java")
print(index)

#元素插入
name.insert(1,"Spring")
print(name)

#在列表尾部插入一个元素
name.append("Baojie")
print(name)

#在列表尾部插入一批元素
name2=["bbjj","hello","nihao"]
name.extend(name2)
print(name)

#元素的删除
del name[0]
print(name)

pop=name.pop(2)
print(pop)
print(name)

name.remove(123)
print(name)

#清空列表

# name.clear()
# print

#统计
count=name.count("bbjj")
print(count)