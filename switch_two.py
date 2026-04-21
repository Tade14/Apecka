#Zadání     list 1-10    2 hodnoty, pozice které prohodíte          #co je to list? proměná do které muhu zdávat hodnoty
nums = []
for i in range (1,11):
    nums.append(i)
    print(nums)
while True:
    a = int(input("který prvek bude první, který chcete vyměnit?"))
    b = int(input("který prvek bude druhý, který chcete vyměnit?"))

    if a != b and b >= 0 and a >= 0 and a < len(nums) and b < len(nums): #a se nsmí rovnat b potom b se je vetsi nez nula, a... , a musi být větší než nums, b musí...
        break

pom = nums[a]
nums[a] = nums[b]
nums[b] = pom

print(nums)