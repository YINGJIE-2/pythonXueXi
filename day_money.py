import time
from datetime import datetime

# 每日收入设定（单位：元）
DAILY_INCOME = 100

# 工作时间（小时）
WORKING_HOURS = 9  # 从早上9点到晚上6点共9小时

# 计算每秒收入（元/秒）
SECONDS_PER_DAY = WORKING_HOURS * 60 * 60
EARNINGS_PER_SECOND = DAILY_INCOME / SECONDS_PER_DAY


def get_today_working_seconds():
    """计算当天从9点到当前时刻的工作秒数"""
    now = datetime.now()
    today_9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
    today_6pm = now.replace(hour=18, minute=0, second=0, microsecond=0)

    # 如果当前时间在9点之前，返回0
    if now < today_9am:
        return 0
    # 如果当前时间在6点之后，返回整个工作时间段的秒数
    elif now > today_6pm:
        return SECONDS_PER_DAY
    # 否则返回从9点到现在的秒数
    else:
        return (now - today_9am).total_seconds()


def main():
    try:
        print(f"每日收入: {DAILY_INCOME} 元")
        print(f"工作时间: 9:00 - 18:00 ({WORKING_HOURS}小时)")
        print(f"每秒收入: {EARNINGS_PER_SECOND:.6f} 元/秒")
        print("-" * 30)
        print("开始计算收入... (按 Ctrl+C 停止)")

        while True:
            working_seconds = get_today_working_seconds()
            if working_seconds >= SECONDS_PER_DAY:
                # 工作时间已结束
                earnings = DAILY_INCOME
                status = "工作时间已结束"
            elif working_seconds <= 0:
                # 工作时间还未开始
                earnings = 0
                status = "工作时间未开始"
            else:
                # 工作进行中
                earnings = working_seconds * EARNINGS_PER_SECOND
                status = "工作进行中"

            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"\r{current_time} - 已赚取: {earnings:.6f} 元 | {status}", end="")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n程序已停止")


if __name__ == "__main__":
    main()