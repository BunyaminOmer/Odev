# 1-100 e kadar

x = 1
while x <= 1000:       # Sayı 100 den küçük olunca döngü devam eder.
    if x % 2 == 1:    # Sayı 2 ye tam bölününce modu 1 çıkarsa if bloğu çalışır.
        print(f"sayı tek  : {x}")
    else:
        print(f"sayı çift : {x}")    # Eğer if bloğunun şartı çalışmazsa else bloğu çalışır ve printi yazdırır.
    x += 1    # Sayıya sürekli bir sayı eklediği için bu döngü en sonunda biter.

print("Bitti...")


name = "" # False
while not name.strip():    # Strip metodu ile boşluk koyulunca kabul etmez.
    name = input("İsminizi giriniz : ")

print(f"Merhaba, {name}")