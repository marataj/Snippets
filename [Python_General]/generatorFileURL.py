import os
import requests

path = r"D:/temp/temp"

def genGetFiles(dir):
    for i in os.listdir(dir):
        yield os.path.join(dir,i)
        

def genGetFileLines(filePath):
    file=open(filePath) 
    for line in file:
        yield line.replace("\n","")
        
def checkWebPage(url):
    try:
        exit_code=requests.get(url)
        if exit_code.status_code==200:
            return True
        else:
            return exit_code
    except:
        return False

try:
    os.mkdir('D:/temp/temp')
except:
    pass
 
with open('D:/temp/temp/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')
 
with open('D:/temp/temp/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')


for i in genGetFiles(path):
    for j in genGetFileLines(i):
        print("Plik - {}, {}".format(j,checkWebPage(j)))

