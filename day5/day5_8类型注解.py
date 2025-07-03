import random

var1: int = 5
var2: bool = True
var3: str = "123"


class Student:
    pass


stu: Student = Student()

my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"苹果": 1999}

my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int,int,int] = (1, 2, 3)

# 注释注解

var_1 = random.randint(1, 10)  # type:int
