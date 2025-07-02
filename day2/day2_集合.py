my_set={"黑马程序员","鲍杰","学Python","黑马程序员","鲍杰","学Python"}
#集合元素不重复,自动去重
print(my_set)

my_set2=set()
print(my_set2)

#集合不支持下标访问

#添加元素
my_set.add("nihao")
print(my_set)

#移除元素

my_set.remove("鲍杰")
print(my_set)

#随机取出一个元素

resout=my_set.pop()
print(resout)
print(my_set)

#清空

my_set.clear()
print(my_set)

#取差集

set1={1,2,3,4,5}
set2={1,4,3,4,6}
set3=set1.difference(set2)
print(set3)