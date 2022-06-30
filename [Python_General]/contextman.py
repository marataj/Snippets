import os
import zipfile
import requests

class FileFromWeb:
    def __init__(self,url,temp_file):
        self.url=url
        self.tempFile=temp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tempFile,"wb") as file:
            file.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == FileNotFoundError:
            print("Blad")
            return True

with FileFromWeb(r"https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip","D:/temp/temp/euroxref.zip") as f:
    with zipfile.ZipFile(f.tempFile,'r') as z:
        a_file= z.namelist()[0]
        print(a_file)
        os.chdir("D:/fhdfghd")
        z.extract(a_file,".",None)

##with open("D:/temp/temp/temp.txt","wb") as file:
##    file.
