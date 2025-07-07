"""
数据定义的类
"""


class Record:

    def __init__(self,date,order_id,money,province):
        self.date = date            # 订单日期
        self.order_id = order_id    # 订单编号
        self.money = money          # 订单价格
        self.province = province    # 订单属地

    def __str__(self):
        return f"{self.date},{self.order_id},{self.money},{self.province}"
