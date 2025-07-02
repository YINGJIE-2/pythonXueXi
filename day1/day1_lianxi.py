name='黑马程序员'
stock_price=11.34
stock_code='001522'
stock_price_hangmen=1.3
growth_day=16
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是%.2f,经过%d天后，股价达到了%.2f"%(stock_price_hangmen,growth_day,stock_price+stock_price_hangmen*growth_day))
