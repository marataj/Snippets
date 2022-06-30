import math
import itertools
import os

path=r"D:/temp"

def ScanTree(path):
    for i in os.scandir(path):
        if os.path.isdir(i):
            yield i
            yield from ScanTree(i.path)
            
        else:
            yield i
lista=[]
listing=ScanTree(path)


listing=sorted(listing,key=lambda x:os.path.isdir(x))

for ki,elementy in itertools.groupby(listing, key=lambda x:os.path.isdir(x)):
    print(ki,len(list(elementy)))

print(listing)

