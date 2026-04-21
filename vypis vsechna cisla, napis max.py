max = int(input("Zadejte cislo"))
for i in range(9):
    cislo = int(input("Zadejte cislo"))
    if cislo > max:
        max = cislo
print("Maximální zadané číslo bylo", max)