name = "Sadık Turan"

for letter in name:
    if letter == "a":      # Eğer söylenen stringde a harfi varsa continue yoksa break
        continue           # continue söylenen şeyi siler ama devam eder break ise söylenen şeyle beraber devamını getirmez. 
    print(letter)

x = 0

while x < 5:
    x += 1
    if x == 2:    # x 2 ye eşitse continue
        continue
    print(x)
    
# 1- 100 e kadar tek sayıların toplamı

x = 1
result = 0

while x <= 100:
    x +=1               # Sürekli sayıya 1 ekler
    if x % 2 == 1:      # x 2 ye tam bölündüğünde mod 1 e eşitse continue 
        continue
    result += x

print(f"toplam : {result}")    # tek sayıların toplamı burada f string ile yazdırılır.