cislo = int(input("Zadejte číslo"))
pocet=0
while cislo != 1:
    print(cislo)
    if cislo%2==0:
      cislo = cislo //2
    else:
      cislo=3 * cislo+1
    pocet=pocet+1
print(1)
print("pocet",pocet)

    


