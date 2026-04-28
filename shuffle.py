#máme pole 12345 a vybereme danou honotu kterou vyndame a tim se to pole odkud jsme vzali to cislo zkratilo treba vememe 5 a bude mit pole jenom 1234
from random import randint 
cards = list(range(1,33))
shuffled = []
print(cards)
while cards:
    shuffled.append(cards.pop(randint(0,len(cards)-1)))#tady jsem získlali od 0 do největšího čísla
#zde řekneme at se podiva na karty a prikazem pop nam vynda kartu na tezo pozici
print(cards)
print(shuffled)







