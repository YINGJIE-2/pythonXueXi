def test_fun(compute):
    resout=compute(1,4)
    print(resout)

def compute(x,y):
    return x+y

test_fun(compute)