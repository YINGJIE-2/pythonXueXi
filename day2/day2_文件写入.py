import time
"""
w写入，如果文件不存在则创建文件，如果文件存在且有内容，再次打开会清空内容
"""
f=open("测试2.txt","w",encoding="utf-8")
f.write("Hello World") #将内容写入内存
f.flush() #将内存中的数据写入磁盘，刷新操作
time.sleep(100000)

