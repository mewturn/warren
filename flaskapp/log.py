import datetime

def getCurrentTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
def writeLog(line):
    logfile = "log.txt"
    
    prefix = "[%s] " % (getCurrentTime())
    suffix = "\n"
    
    with open(logfile, "a", encoding="utf-8") as log:
        log.write(prefix + line + suffix)
