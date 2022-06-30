from doctest import Example
import os
import sys

line=input("podaj akceptowalna cene")
filePath=input("Podaj sciezke do pliku")
try:
    with open(filePath, "w") as file:
        file.writeline(line)
except Exception as e:
    print("Error {}".format(e))
   
