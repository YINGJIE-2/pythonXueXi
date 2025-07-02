def name_Test(name,age,sex="女"):
    print(f"你的名字是{name}，你的年龄是{age}，你的性别是{sex}")

name_Test("josen","18","男")
name_Test("mixx","18",)

#不定长参数  默认参数为元组

#不定长  位置不定长*  类元组
def name_Test2 (*args):
    print(args)

name_Test2(1,3,2,"你还",True)

#不定长  关键字不定长**  类字典

def user_info(**args):
    print(args)

user_info(name="xiaoming",age=19)