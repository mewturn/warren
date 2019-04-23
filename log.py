import datetime
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) # Application top
logfile = os.path.join(APP_ROOT, "milton.log")

def getCurrentTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def writeLog(line):
    prefix = "[%s] " % (getCurrentTime())
    suffix = "\n"
    with open(logfile, "a", encoding="utf-8") as log:
        log.write(prefix + line + suffix)
