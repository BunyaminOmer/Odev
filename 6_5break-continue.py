name = "Sadık Turan"

for letter in name:
    if letter == "a":
        continue           # continue söylenen şeyi siler ama devam eder break ise söylenen şeyle beraber devamını getirmez. 
    print(letter)

x = 0

while x < 5:
    x += 1
    if x == 2:
        continue
    print(x)
    
# 1- 100 e kadar tek sayıların toplamı

x = 1
result = 0

while x <= 100:
    x +=1
    if x % 2 == 1:
        continue
    result += x

print(f"toplam : {result}")