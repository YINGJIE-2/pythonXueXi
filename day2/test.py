import time
from datetime import datetime, timedelta


def get_today_working_seconds():
    """计算当天从9点到当前时刻的工作秒数"""
    now = datetime.now()
    today_9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
    today_6pm = now.replace(hour=18, minute=0, second=0, microsecond=0)

    print(f"\r距离下班还剩 {(today_6pm - now).total_seconds():.0f}秒",end="")  #时间差转换为秒

while True:
    get_today_working_seconds()
