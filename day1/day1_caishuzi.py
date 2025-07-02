import random

num=random.randint(1,10)
# print(num)
a=int(input("请输入第一次猜想的数字："))

if a == num:
    print("恭喜第一次就猜对了")
else:
    if a>num:
        print("猜大了")
    else:
        print("猜小了")
    a = int(input("请输入第二次想猜的数字："))
    if a == num:
        print("恭喜第二次就猜对了")
    else:
        if a > num:
            print("猜大了")
        else:
            print("猜小了")
        a = int(input("请输入第三次想猜的数字："))
        if a == num:
            print("恭喜第三次猜对了")
        else:
            if a > num:
                print("猜大了，游戏结束")
            else:
                print("猜小了，游戏结束")





