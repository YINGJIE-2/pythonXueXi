class Student:
    name = None
    id = None
    age = None

    def say_hi(self):
        print(f"大家好,我是：{self.name},学号是：{self.id},我的年龄是{self.age}")

    def say_hi2(self,msg):
        print(f"大家好,我是：{self.name},学号是：{self.id},我的年龄是{self.age},我想说：{msg}")


sut1 = Student()
sut1.name="Baojie"
sut1.id=220663118
sut1.age=21
sut1.say_hi()
sut2 = Student()
sut2.name="Bao"
sut2.id=220663118
sut2.age=22
sut2.say_hi2("woshihhh")
