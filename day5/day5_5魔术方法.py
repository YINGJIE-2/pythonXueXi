class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 字符串魔术方法
    def __str__(self):
        return f"学生姓名：{self.name}学生年龄：{self.age}"

    # __it__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __ie__魔术方法
    def __le__(self, other):
        return self.age < other.age
    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("鲍杰", 22)
stu2 = Student("保洁", 22)
print(stu2 == stu1)
