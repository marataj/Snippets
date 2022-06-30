import pickle
import os
import glob

dirPath=r"C:\skrypty"

class Cake:

    knownTypes=['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    def __init__(self, name, kind, taste, additives, filling,isGlutenFree):

        self.name = name if Cake.knownTypes.count(name) else "other"
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__isGlutenFree=isGlutenFree
        self.__text=""
        Cake.bakery_offer.append(self)

    def GetText(self):
        return self.__text

    def SetText(self,newText):
        if self.kind=="cake":
            self.__text=newText
            print("Text changed to {}".format(newText))
        else:
            print("Change of text is not available")

    NewText=property(GetText,SetText,None,)
    
    def ShowInfo(self):
        print(self.name.upper())
        print(self.filling)
        if self.additives :
            print(self.additives)

    def SetFilling(self,fill):
        self.filling=fill
    def AddAditives(self,addit=[]):
        self.additives.extend(addit)

    def SaveToFile(self,path):
        fileName=self.name+".bakery"
        f=os.path.join(path,fileName)
        file= open(f,'wb')      
        pickle.dump(self,file)
        print("Object has saved to file {}".format(f))
        file.close()

    @classmethod
    def ReadFromFile(cls,path):
        with open(path,'rb') as file:
            print("Downloading object...")
            obj = pickle.load(file)
            Cake.bakery_offer.append(obj)
            return obj

    @staticmethod
    def GetBakeryFiles(dirPath):
        bakeryList=glob.glob(os.path.join(dirPath,"*.bakery"))
        print("Program uploaded list of bakery file: {}".format(bakeryList))
        return bakeryList
       

cake01 = Cake('Vanilla Cake','muffin', 'vanilla', ['chocolade', 'nuts',"lools"], 'cream',False)
cake01.NewText = "100 lat"
print(cake01.NewText)
cake01.SaveToFile(dirPath)
cake02=Cake.ReadFromFile(r"C:\skrypty\other.bakery")
cake02.ShowInfo()
print(Cake.GetBakeryFiles(dirPath))

