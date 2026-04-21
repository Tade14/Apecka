import random
pocet = 0
while True:
    x = int(input("zadejte cislo v rozmezí 1-6"))
    if 0 < x < 7:
        break
while True:
    rand1 = random.randint(1,6)
    rand2 = random.randint(1,6)
    print(rand1,rand2,x)
    if rand1 != rand2 or x!= rand1:
        pocet += 1
    else:
        break
   
print("trvlo to",pocet)