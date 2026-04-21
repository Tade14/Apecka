#veme vec z durheho pole a da ho do druheho pole ale kdyz si vemu vec ktereou uz jsem vzal tak nic nedelam a napisu, chci pocet kroku 
#postup: 1)naplň list 1-32 2)losuj náhodnou pozici 3)kopíruj pozici do nového místa 4)počítej počet pokusů
#postup podle učitele
import random
cards = list(range(1,33))
shuffled = []
pocet = 0
print(cards)
for _ in range (len(cards)):
    while True:
        card = random.randint(0, 31)
        pocet += 1 
        if cards[card]!= None:
            shuffled.append(cards[card])
            cards[card] = None
        
            break
print(shuffled)
print("pokusy", pocet)