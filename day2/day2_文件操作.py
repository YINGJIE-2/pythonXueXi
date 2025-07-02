# f = open("测试.txt","r",encoding="utf-8")
# print(f.read())
# print(f.read(10))
# lines=f.readlines()
with open("测试.txt","r",encoding="utf-8") as f:

    for lines in f:
      print(lines)
f.close()
