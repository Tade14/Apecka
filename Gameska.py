unik = False
pokusy = 3
import random 
číslo=random.randint (100,999)
   
while pokusy>0 and not unik:

    print("Máš", pokusy, "pokusy")
    print("1 - Prohledat šuplík")
    print("2 - Podívat se do skříně")
    print("3 - Podívat se pod postel\n")
    
    volba = input("Co uděláš?")

    if volba == "1":
        print("Našel jsi kód", číslo)
    elif volba == "2":
        kód = int(input("Zadejte kód"))
        if kód == číslo:
            unik = True 
        else:
            print ("Špatný kód")
            pokusy=pokusy-1 

    elif volba == "3":
        print("Nic tu není")
    else:
        print("Neplatná možnost")

if unik == True:
    print("Unikl jsi z místnosti")
else:
    print("prohrál jsi")