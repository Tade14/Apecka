import random
def vygeneruj_zbran(material):
    zbran = ("mec","luk","stit")
    druhz = random.choice(zbran)
    poskozeni = random.randint(10,100)
    return material + " " + druhz + "  " + " (+ " + str(poskozeni) + " k poskozeni)"
print(vygeneruj_zbran("železný"))
print(vygeneruj_zbran("dřevěný"))