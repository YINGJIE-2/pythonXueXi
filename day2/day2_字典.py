# dict={
#     key:value
#     key:value
#      }###           key不可重复

my_dict={
    "小米13":1299,
    "华为p90":1399,
    "苹果13":1499
}
my_dict2=dict()

print(my_dict)
print(my_dict["小米13"])

#定义嵌套字典
stu_score_dict={
    "王力宏":{
        "语文":89,
        "数学":78,
        "英语":88
    },
    "刘德华":{
        "语文":99,
        "数学":68,
        "英语":89
    },
    "周杰伦":{
        "语文":30,
        "数学":67,
        "英语":69
    }
}

print(stu_score_dict)
score=stu_score_dict["刘德华"]["英语"]
print(f"刘德华的英语成绩是：{score}")