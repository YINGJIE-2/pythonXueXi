class Phone:
    IMEI = None
    producer = "ITCARE"

    def call_by_5g(self):
        print("父类5g通话")


class MyPhone(Phone):
    producer = "ITHEiUMA"   #复写父类的成员属性

    def call_by_5g(self):

        print("开启cpu单核模式，确保续航")
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("开启5g通话")
        print("关闭cpu单核模式，确保性能")



phone = MyPhone()
print(phone.producer)
phone.call_by_5g()