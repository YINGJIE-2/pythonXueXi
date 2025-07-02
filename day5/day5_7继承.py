# 单继承



class Phone():
    IMEI=None
    producer="ITCATE"

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id="100001" #面部识别

    def call_by_5g(self):
        print("5g通话")

# phone=Phone2022()
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()

# 多继承




class NFC:
    nfc_type="第五代"
    producer = "HM"
    def read_card(self):
        print("nfc读卡")

    def write_card(self):
        print("nfc写卡")


class RemoteControl:
    rc_type="红外遥控"
    def control():
        print("红外遥控开启了")

class MyPhone(Phone,NFC,RemoteControl):
    pass

phone=MyPhone()

phone.call_by_4g()
phone.write_card()
phone.control()
phone.read_card()
print(phone.producer)