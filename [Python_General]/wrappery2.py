import os
import functools
import datetime

fileDir=r'D:\temp'
testPath=r'D:\temp\test.txt'
logPath=r'D:\temp\logs.txt'
logPath2=r'D:\temp\logs2.txt'


def WrapperWithParameter(logFile):
    def WrapperToKnownFile(func):
        def function(*args,**kwargs):
            print("Wrapped function started")
            with open(logFile,"a+") as file:
                file.write("Action {} executed on {} on {}".format(func.__name__,args[0],datetime.datetime.now()))
            result = func(*args,**kwargs)
            return result
        return function
    return WrapperToKnownFile

@WrapperWithParameter(logPath2)
def FileEventHandler(path,event="create"):
    try:
        if event == "create":
            print('creating file {}'.format(path))
            open(path,"w+")
        elif event == "delete":
            print('deleting file {}'.format(path))
            os.remove(path)
    except:
        print("Wystapil blad")
@WrapperWithParameter(logPath2)
def CreateFile(path):
    print('creating file {}'.format(path))
    open(path,"w+")
@WrapperWithParameter(logPath)   
def DeletingFile(path):
     print('deleting file {}'.format(path))
     os.remove(path)
        

CreateFile(testPath)    
DeletingFile(testPath)


