
"""
__all__作用于导入时候的*
"""

__all__=["fun1"]
def fun1(x,y):
    print(x+y)

def fun2(x,y):
    print(x*y)

# if __name__ == '__main__':
#     fun1(1,4)