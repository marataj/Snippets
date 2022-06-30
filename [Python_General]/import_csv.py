import csv
 
with open('d:/temp/doc.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            print("The end of file")
            break;

    #for row in csvreader:
      #  print('|'.join(row))
