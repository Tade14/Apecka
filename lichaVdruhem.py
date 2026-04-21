#Zadání : list od 1 do 20 budou dva a jeden list bude lichý a druhý bude sudý
nums = list(range(1,21))
licha = []
suda = []
#zde si uěláme co budem potřebovat na výběr sudých čísel
for num in nums: #projde nám naše pole a uloží ho do naší proměný num
    if num % 2 == 0:   #děleno dvěma znamená že to je sudé
        suda.append(num) #číslo které procházíme tedy ty která jsou dělitelné dvěma se nám přidají do proměné sudá
    else:
        licha.append(num)
print("sudá:", *suda, sep= " | ", end= " | ")
print()
print("lichá:", *licha, sep= " | ", end= " | ")
