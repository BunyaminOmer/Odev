# 1-100 e kadar

x = 1
while x <= 100:       # Sayı 100 den küçük olunca döngü devam eder.
    if x % 2 == 1:
        print(f"sayı tek  : {x}")
    else:
        print(f"sayı çift : {x}")
    x += 1    # Sayıya sürekli bir sayı eklediği için

print("Bitti...")


name = "" # False
while not name.strip():    # Strip metodu ile boşluk koyulunca kabul etmez.
    name = input("İsminizi giriniz : ")

print(f"Merhaba, {name}")