colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

allCards =[]

for each in colors:
    for fig in figures:
        allCards.append(each+" "+fig)

print(allCards)

import random

random.shuffle(allCards)
print(allCards)
player1=[]
player2=[]

for i in range(0,len(allCards),2):
    player1.append(allCards[i])
    player2.append(allCards[i+1])

print(player1)
print(player2)

