
try:
    f=open("hh.txt","r",encoding="utf-8")
except:
    print("出现异常，因为文件不存在，我将把open的模式改为w")
    f=open("hh.txt","w",encoding="utf-8")

f.close()

#捕获指定异常

try:
    print(name)
except NameError as e:
    print("变量未定义")
    print(e)

#捕获多个异常
try:
    print(name)
except (NameError,ZeroDivisionError) as e:
    print("出现变量未定义 或者 除零异常")

#捕获全部异常

try:
    print(name)
except Exception as e:
    print("出现异常")
else:
    print("<UNK>")
finally:
    print("<UNK>")