import schedule
import time
from dailyaccuracy import DailyAccuracy
import datetime
from tools.gchat_logging import send_to_g_chat

controller = DailyAccuracy()


def check_time_and_send():
    now = datetime.datetime.now().time().strftime("%H:%M")
    target_times = ["11:00", "02:00"]  # Set your target times here

    if now in target_times:
        send_to_g_chat(data=f"Schedular is started at {datetime.datetime.now()}")
        controller.accuracy_update()

    else:
        print(f"checking schedular for perfect time {now} = {target_times}")


# schedule.every().day.at(now).do(send_telegram_message())
schedule.every(1).minutes.do(check_time_and_send)

while 1:
    schedule.run_pending()