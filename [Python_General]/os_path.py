import os
filePath=input("Put file path:\t")
while not os.path.isfile(filePath):
    print("Wrong path, please put it again")
    filePath=input("Put file path:\t")

dirName=os.path.dirname(filePath)
print("Nazwa katalogu to %s" %(dirName))

fileNamePl="webPl.txt"
fileNameOther="webOther.txt"



filePl=open(os.path.join(dirName,fileNamePl),"w")
filePlBuf=[]
fileOther=open(os.path.join(dirName,fileNameOther),"w")
fileOtherBuf=[]

webAdresses=[]
with open(filePath,"r") as file:
    webAdresses=file.readlines()
print(webAdresses)
for adress in webAdresses:
    adress=adress.replace("\n","")
    if  adress.find(".pl") != -1:
        print(adress," jest adresem z polski")
        filePlBuf.append(adress+"\n")
    else:
        print(adress," nie jest adresem z polski")
        fileOtherBuf.append(adress+"\n")


filePl.writelines(filePlBuf)
fileOther.writelines(fileOtherBuf)
filePl.close()
fileOther.close()
