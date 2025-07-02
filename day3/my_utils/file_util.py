def print_file_info(file_name):
    f=None
    try:
        f = open(file_name,"r",encoding="utf-8")
        read_file=f.read()
        print(read_file)
    except:
        print("文件不存在")
    finally:
        if f:
            f.close()

def append_to_file(file_name,data):
    f=open(file_name,"a+",encoding="utf-8")
    f.write(data)
    f.close()