while True:

  x = int (input("zadejte první číslo"))
  y = int (input("Zadejte druhé číslo"))
  print ("1.Součet \n2. Součin \n3. Rozdíl \n4. Podíl")
  operace = input("Vyberte cislo operace, kterou chcete porvest")
  match operace:
    case 1:    
        soucet = x + y 
        print (soucet)
    case 2:
        soucin = x - y 
        print (soucin)
    case 3: 
        rozdil = x * y 
        print (rozdil)
    case 4:
        if y == 0:
           print ("Nelze delit nulou")
        else:
            podil = x / y 
            print(podil)
    konec = input("Prejete si ukoncit program? Y/N")
     if konec.lower ()== "y" : 
    break 
