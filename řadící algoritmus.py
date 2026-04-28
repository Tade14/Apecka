#1.Naplň 10 náhodných čísel 2.Najdi minimální index 3.Opakuj
from random import randint

cards = [] 
for _ in range(10):
    cards.append(randint(1,50)) #vytvoreno 10 random cisel ofd 1 do 50

print(cards)
for i in range(len(cards)):
    min_index = i
    for j in range(i, len (cards)): #projde cisla takovy ktere jsou v cards
        if cards[j] < cards[min_index]:
            min_index = j
    cards[i], cards[min_index] = cards[min_index], cards[i]
    print(cards)  