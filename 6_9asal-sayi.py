"""
Soru : Girilen bir sayının asal sayı olup olmadığını bulun.
** Asal sayı 1 ve kendisi hariç tam böleni olmayan
    sayılara denir.
"""

sayi = int(input("Sayı : "))    # Sayı inputla alınır.
asalmi = True

if sayi == 1:
   asalmi = False

for i in range(2, sayi):
    if (sayi % i == 0):    # Sayı sıfıra eşit çıkarsa 
        asalmi = False
        break

if asalmi:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")