import os
import time

while True:
    
    dir=input("Wpisz sciezke do pliku\n")
    if not os.path.exists(dir):
        print("Błędna sciezka !\n")
    else:
        break;

while True:
    
    dir2=input("Wpisz nazwe pliku\n")
    if not os.path.exists(os.path.join(dir,dir2)):
        print("Błędna sciezka !\n")
    else:
        break;

print("Wyszedles z petli\n")
