while True:

  x = int (input("zadejte první číslo"))
  y = int (input("Zadejte druhé číslo"))
  soucet = x + y 
  print (soucet)
  soucin = x - y 
  print (soucin)
  rozdil = x * y 
  print (rozdil)

  if y == 0:
    print ("Nelze delit nulou")
  else:
    podil = x / y 
    print(podil)
    konec = input("Prejete si ukoncit program? Y/N")
    if konec.lower ()== "y" : 
       break 