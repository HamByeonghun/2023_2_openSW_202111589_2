import telegram
import asyncio
import schedule
import time
import pytz
import datetime


def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    #시간 제한 설정
    if now.hour >= 23 or now.hour <= 6:
        return

    print("current time = ", str(now))
    #텔레그램 토큰 코드와 대화방
    token = "6737444059:AAEaI28MZZY0hzoHS4Y8H9Oi1rMK2QOcgFA"
    bot = telegram.Bot(token = token)
    public_chat_name = '@k_2023_opensw'
    id_channel = asyncio.run(bot.sendMessage(chat_id=public_chat_name,text="alarm arrived!!!!!")).chat_id
    print(id_channel)

schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)