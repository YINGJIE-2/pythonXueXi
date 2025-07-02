#字符串也不能修改

str_name="hello world"
value=str_name[6]
print(value)

#替换方法，本身不变

new_str_name=str_name.replace("world","世界")
print(new_str_name)

#字符串分割，本身不变

my_str="hello Python itheima world"
my_strlist=my_str.split(" ")
print(my_strlist)

# #字符串规整
# my_str="   hello Python itheima world   "
# my_strlist=my_str.strip()
# print(my_strlist)
#
# #统计字符串出现的次数
#
# my_str="hello Python itheima world"
# count=my_str.count("Python")
# print(count)