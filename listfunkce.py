batoh = ["lektvar , klacík ,meč , zlato"]
#spocitej pocet lektvaru v batohu
def pocitani_lektvaru(soucet):
    pocet = 0
    for staff in soucet:
        if staff == "lektrvar":
            pocet +=1        
    return pocet
print(f"Máš {pocitani_lektvaru(batoh)} lektvarů")

