class Student:
    name=None
    age=None
    tel=None

    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel

    def print_info(self):
        print(f"我的姓名是：{self.name}，我的年龄是：{self.age}，我的电话号码是：{self.tel}<UNK>")



stu1=Student(name="Baojie",age=21,tel="220312")
stu1.print_info()
