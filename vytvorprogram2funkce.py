#Vytvor program, ktery bude obsahovat 2 funkce ,,zobraz_menu" a ,,vygeneruj_nepritele".Program bude zobrazovat meu s volbami (1-vytvor postavu, 2-konec hry).V případě 
#zadání jiného čísla tuto skutecnou oznami uzivateli.V pripade zadani 1 se zavola funkce ,,vygeneruj_mnepritele" ktera ma parametr pro jmeno.Funkce vrati retezec napr. 
#,,Nepritel Grogu je vlk ma 30 hp" Jmeno zadava uzivatel
import random
def zobraz_menu():
    print("---Hlavní menu---")
    print("1 - vytvor postavu")
    print("2 - konec hry")
while True:
    zobraz_menu()
    def vygeneruj_nepritele(name):
        druhy = ["skřet","Troll","Vlk"]
        druh = random.choice(druhy)
        zivoty = random.randint(20,100)
        return "Nepřítel " + name + " je " + druh + " a má " + str(zivoty) + "HP"
    volba = input("Co chces udelat?(napis cislo):")
    if volba == "1":
        print("Vygeneruj postavu")
        print(vygeneruj_nepritele(input("Zadejte jmeno nepritele")))
    elif volba == "2":
        print("vypinam hru")
        break
    else:
        print("tuhle volbu neznam")
