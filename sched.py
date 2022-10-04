import schedule
import time
import os

def func():
    print("Hello Geek")

schedule.every(1).minutes.do(func)

while True:
    schedule.run_pending()
    
    time.sleep(1)