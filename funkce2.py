#vytvorte funkci kde rozhodne jestli je clovek dost stary na nakup hry 12
def rozhodovani(vek, jmeno):
    if vek >= 12:
          return jmeno + "je dostatecne stary pro nakup"
    else:
         return jmeno + "je prilis mlady na nakup"
print(rozhodovani(14,"Přemysl"))
print(rozhodovani(10,"Hugo"))
