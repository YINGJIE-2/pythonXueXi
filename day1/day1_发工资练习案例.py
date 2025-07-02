import random

sum_salary=10000
for i in range(1,21):
    jixiao = random.randint(1,10)
    if jixiao<5:
        print(f"员工{i}，绩效分{jixiao}，低于5，不发工资，下一位")
    else:
        sum_salary-=1000
        if sum_salary<0:
            print("工资发完了，下个月领取把")
            break
        print(f"向员工{i}发放1000元工资，账户余额还剩：{sum_salary}")

