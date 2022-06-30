import datetime as dt


class TripException(Exception):
    def __init__(self,text,description):
        super().__init__(text)
        self.description=description

    def __str__(self):
        return "{}, {}".format(super().__str__(),self.description)
        

 
class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    

    @classmethod
    def publishOffer(cls,tripsList):
        listOfErrors=[]
        for e in tripsList:
            try:
                e.check_data()
            except ValueError as ex:
                listOfErrors.append({e.symbol:ex})
                print("Error occured in element: {}.\nError: {}\n".format(e.symbol,ex))
            except Exception as ex:
                listOfErrors.append({e.symbol:ex})
                print("Error occured in element: {}.\nError: {}\n".format(e.symbol,ex))
        if len(listOfErrors):
            raise TripException("The list of trips has errors", "Description of Error")
        #assert len(listOfErrors)==0, "Tttttttttthe list of trips has errors:{}".format(listOfErrors)
            
        print("The offer will be published...")
            
 
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]

try:
    print("Checking the offer...")
    Trip.publishOffer(trips)
    print("Done")

except Exception as exc:
    print("The checked offer has a issue:\n{}\n".format(exc))
