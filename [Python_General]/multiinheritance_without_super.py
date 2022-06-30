from datetime import date
from datetime import timedelta  
class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
 
    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)
 
class Promo():
 
    def __init__(self, name, discount, start_date, end_date, minimal_order):
 
        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date =  end_date
        self.minimal_order = minimal_order
 
    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)
 

class PromoCake(Promo,Cake):
    def __init__(self,name,discount,start_date,end_date,minimal_order,kind, taste, additives, filling):
        Promo.__init__(self,name, discount, start_date, end_date, minimal_order)
        Cake.__init__(self,name, kind, taste, additives, filling)

    
 
cake = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake.show_info()
 
promo10 = Promo("DISCOUNT - no additional conditions", 0.15, date.today(), date.today() + timedelta(days=14),0)
print(promo10.full_name)

promo_cake = PromoCake("nazwa","d","1","2",13,"tr","trus",["brak"],"wisnia")
promo_cake.show_info()