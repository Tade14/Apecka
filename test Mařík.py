tvar = input("Zadejte jaký tvar chcete počítat? čtverce nebo obdelník ")


if tvar == "čtverec":
    x = int(input("Zadejte číslo"))
    obsah = x * x
    obvod = x*4
    print ("Obsah čtverce",obsah)
    print ("Obvod čtverce",obvod)
if tvar == "obdelník":
    x = int(input("Zadejte číslo"))
    y = int(input("Zadejte číslo"))
    obsah1 = x * y
    obvod1 = 2*(x+y)
    print ("Obsah obdelníku",obsah1)
    print ("Obvod obdelníku",obvod1)
    
