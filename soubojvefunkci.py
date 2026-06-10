#souboj--->obrana nebo utok ----> zasah nebo odrazeno
def souboj(utok, obrana):
    if obrana > utok:
        return ("odrazil si utok")
    else:
        return ("zasah")
print(souboj(50 ,35))
print(souboj(20 ,35))
