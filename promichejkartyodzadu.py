#prohodim cislo od konce s nekym random v poli a takhle to bude do kola ale bude chodit od konce
from random import randint
cards = list(range(1,33))
print(cards)
for i in range(len(cards)-1, 0, -1):
    rand = randint(0,i)
    cards[i], cards[rand] = cards[rand], cards[i]
    print(cards)