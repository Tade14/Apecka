#Funkce obsahuje list,v něm jsou typy NPC jako skřet, troll a vlk.Pří zavolání funkce doplníme jméno v rámci funkce přidáníme druh a množství zdraví
#random.choice(list)
#nepřítel jméno je druh a má zdraví
import random 
def vygeneruj_nepritele(name):
    druhy = ["skřet","Troll","Vlk"]
    druh = random.choice(druhy)
    zivoty = random.randint(20,100)
    return "Nepřítel" + name + "je" + druh + "a má" + str(zivoty) + "HP"
print(vygeneruj_nepritele("Grogu"))
print(vygeneruj_nepritele("Yoda"))
