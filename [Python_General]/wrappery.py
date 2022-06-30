import functools
import datetime


def wrapper(func):
    def function(*args,**kwargs):
        timeBefore=datetime.datetime.now().second
        result=func(*args,**kwargs)
        timeAfter=datetime.datetime.now().second
        print("The function durates {} secconds".format(timeAfter-timeBefore))
        return result
    return function

@wrapper
def printYo(n):
    return ("yo"*n)



def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
getWrappedSeq=wrapper(get_sequence)
getWrappedSeq(18)

