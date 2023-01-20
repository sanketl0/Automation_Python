
import schedule
import time
import datetime

def task_Minutes():
    print("Task based on minutes get schedule at :",datetime.datetime.now())

def task_Hour():
    print("Task based on Hour get schedule at :",datetime.datetime.now())

def task_Day():
    print("Task based on day get schedule at :",datetime.datetime.now())

def main():

    print("Inside task schedular:")
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minutes.do(task_Minutes)
    schedule.every(1).hour.do(task_Hour)
    schedule.every().saturday.at("18:00").do(task_Day)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

