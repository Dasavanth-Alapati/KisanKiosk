from django.utils import timezone as tz


class timepass:
   def __init__(self,sec):
       self.year = int(sec/31556952)
       self.month = int(sec/2629746)
       self.day = int(sec/86400)
       self.hour = int(sec/3600)
       self.minute = int(sec/60)
       self.second = int(sec)



def itemage(objtime):
    curtime = tz.now()
    timepassed = curtime - objtime
    timepassed = timepass(timepassed.total_seconds())
    if timepassed.year > 0:
        if timepassed.year > 1:
            return str(timepassed.year)+' years'
        else:
            return str(timepassed.year)+' year'
    elif timepassed.month > 0:
        if timepassed.month > 1:
            return str(timepassed.month)+' months'
        else:
            return str(timepassed.month)+' month'
    elif timepassed.day > 0:
        if timepassed.day > 1:
            return str(timepassed.day)+' days'
        else:
            return str(timepassed.day)+' day'
    elif timepassed.hour > 0:
        if timepassed.hour > 1:
            return str(timepassed.hour)+' hrs'
        else:
            return str(timepassed.hour)+' hr'
    elif timepassed.minute > 0:
        if timepassed.minute > 1:
            return str(timepassed.minute)+' mins'
        else:
            return str(timepassed.minute)+' min'
    else:
        if timepassed.second > 1:
            return str(timepassed.second)+' secs'
        else:
            return str(timepassed.second)+' sec'
