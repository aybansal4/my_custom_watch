#!/usr/bin/python3
import datetime, time, subprocess
def dateAndTime():
    dt = datetime.datetime.now()
    print(f"It is:\n{dt.strftime("\033[32m%H:%M:%S, \033[36m%m/%d/%Y\033[0m")}")
    print("You got this \U0000263A")
    time.sleep(1)
    subprocess.run("clear")
def motd():
    day = (datetime.date.today()).isoweekday()
    if day == 1:
        print("It's Monday, new week, new start!")
    elif day == 2:
        print("Tuesday's here, do something great today!")
    elif day == 3:
        print("Wednesday came, middle of the week; let\'s do something unique!")
    elif day == 4:
        print("Welcome to Thursday, have a laugh and relax!")
    elif day == 5:
        print("Its Friday be thankful for how far in the week we are keep pushing a little longer.")
    elif day == 6:
        print("Sprinkle a little sunshine on your soul for Saturday and have some fun!")
    elif day == 7:
        print("It\'s Sunday, a fun day, but get ready for the new week ahead!")
    else:
        print("I can't seem to find the day of the week, anyhow do something good today.")
def earth():
    subprocess.run(["curl","http://ascii.live/earth"])
if __name__ == "__main__":
    print("we don't have a full interface yet. you can simply import this code as a module and use the functions time() motd() or earth() to see the stuff we have")
