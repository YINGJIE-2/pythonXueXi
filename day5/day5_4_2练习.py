class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address, f):
        self.f = f
        self.name=name
        self.age=age
        self.address=address
        print(f"学生{self.f}信息录入完成，信息为【学生姓名：{self.name}，年龄：{self.age}，地址：{self.address}】")

for i in range(10):
    print(f"当前录入第{i+1}位学生，总共需录入10位学生")
    stu_name=input("请输入学生姓名： ")
    stu_age=input("请输入学生年龄： ")
    stu_address=input("请输入学生地址： ")
    stu=Student(stu_name,stu_age,stu_address,i+1)


