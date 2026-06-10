import random
pole = list(range(1, 33))
pole2 = []
print(pole)
while pole:
    pole2.append(pole.pop(random.randint(0,len(pole)-1)))


print(pole)
print(pole2)    
    

