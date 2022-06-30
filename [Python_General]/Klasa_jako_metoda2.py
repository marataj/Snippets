class NoDuplicate:
    def __init__(self):
        self.list=[]

    def __call__(self,lista):
        for element in lista:
            if self.list.count(element) == 0:
                self.list.append(element)
                print("Element {} apended to the list".format(element))
            else:
                print("Element {} already is on the list".format(element))
        
duplikat = NoDuplicate()
duplikat(["1","2"])
duplikat(["1","2","3"])
print(duplikat.list)
