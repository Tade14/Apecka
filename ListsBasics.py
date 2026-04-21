mylist = ["pomeranč", "jablko", "citron ", "kumqat", "papaja"]
print (mylist)
print(len(mylist))
print(mylist[2])
print(mylist[-1])

duplist = mylist [2:5]
print (duplist)

if "jablko" in mylist:
    print ("jablko tam je")

mylist[2] = "Samice hrabáče"
print(mylist)

mylist.append("mango")
print(mylist)
mylist.insert(1,"banán")
print(mylist)

zeleninalist = ["paprika", "mrkev", "okurka"]
mylist.extend(zeleninalist)
print (mylist)

mylist.remove("kumqat") #odstraní položku podle indexu, pokud není uveden odtraní poslední 
print(mylist)

print(zeleninalist)
zeleninalist.clear() #vyprázdní list
print(zeleninalist)

del zeleninalist #definitivě odstraní list
for i in mylist:
    print(i)

for i in range(len(mylist)):
    print(mylist[i])

abeceda = ["A", "F", "C", "D"]
abeceda.sort()
print(abeceda)

abeceda.sort(reverse=True) #otočí
print(abeceda)

mylist.sort(key=str.lower)
print(mylist)

nums = [100,50,65,82,23]
nums.sort() #seřadí čísla postupně od nejmenšího do největšího
print(nums)
nums.sort(reverse = True) #čísla nám otočí od největšího do nejmenšího
print(nums)


mylist2 = mylist #list2 odkazuje na list, když něco měním ve 2 bude to i v 1

print(mylist)
print(mylist2)
mylist2[0]= "malina"
print(mylist2)
print(mylist)

copylist = mylist.copy()
copylist[0] = "ořech"
print(mylist)
print(copylist)


