import random

num=random.randint(1,100)
a=int(input("请输入猜想的数字："))
i=0
while True:
    i+=1
    if a==num:
        print(f"恭喜你第{i}次猜对了！")
        break
    elif a>num:
        print("猜大了")
    else :
        print("猜小了")
    a=int(input("请再次输入猜想的数字："))