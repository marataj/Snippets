def generator(products, promotions, customers):
    for i in products:
        for x in promotions:
            for y in customers:
                item_to_return = "{} - {} -{}".format(i,x,y)
                yield item_to_return
        
 
        
 
 
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]
 

 
for c in generator(products,promotions,customers):
    print(c)
