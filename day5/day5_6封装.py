class Phone:

    __current_voltage=2  #私有变量

    def __keep_single_core(self):  # 私有方法
        print("让cpu单核工作")

    def call_5g(self):
        if self.__current_voltage > 5:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话")


ph=Phone()
ph.call_5g()