import random

def generateTastes(taste1,taste2,taste3):

    for i in range(9):
        a=random.randint(0,100)
        b=random.randint(0,100-a)
        c=100-(a+b)

        yield("***********\n{} taste is: \n{}:\t{}\n{}:\t{}\n{}:\t{}\n".format(i+1,taste1,a,taste2,b,taste3,c))

for i in generateTastes("Slodki","slony","kwasny"):
    print(i)
