
import datetime
import sys
import time
import schedule


def fun():
    print("Inside fun at time:",datetime.datetime.now())

def script_Terminator():
    print("schedule is exit")
    sys.exit()

def main():

    print("Inside task schedular:")

    print("Current time is :",datetime.datetime.now())
    
    schedule.every(1).seconds.do(fun)
    schedule.every(8).seconds.do(script_Terminator)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

