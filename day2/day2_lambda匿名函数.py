#只能临时使用一次

def test_fun(compute):
    resout=compute(1,4)
    print(resout)

test_fun(lambda x,y:x+y)