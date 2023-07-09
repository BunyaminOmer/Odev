"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
    buldurmaya çalışın (hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
       üzerinden hesaplansın.
"""

import random

sayi  = random.randint(1,100)
can = int(input("Kaç hakkınız olmasını istersiniz : "))
hak = can    # hak sayısı can sayısıyla eş çalışmalı ve inputtan gelen bilgiyi hak ile eşitlemeli
sayac = 0    # Her hamleyi sayar

while hak > 0:
    hak -= 1    # Verilen haktan sürekli bir eksiltir.
    sayac += 1  # Sayaca sürekli bir hamle yapıldığında sürekli hamle sayısı yazsın.
    tahmin = int(input("Tahmini sayıyı giriniz : "))   # Tahmini sayıyı yazarız

#                                                            100 den inputta verilen can sayısı 100 e bölünür
# 
#                                                                               ↓ Sonuçları çarpar
#                                                                               ↓       ↓    
#                                                                               ↓       ↓     Şimdiki hamle dahil değil doğru cevaptaki
#                                                                               ↓       ↓       ↓
#                                                                               ↓       ↓       ↓
#                                                                               ↓       ↓       ↓
    if sayi == tahmin: 
        print(f"Tebrikler! {sayac}. defada bildiniz. Toplam puanınız : {100 - (100/can) * (sayac-1) }")
        break    # Oyunu kazandığı için son verir.
    elif sayi > tahmin:    # Söylenen sayı büyükse Daha yüksek bir sayı girin çıkar.
        print("Daha yüksek bir sayı girin")    
    else:                  # Söylenen sayı büyükse Daha düşük bir sayı girin çıkar
        print("Daha düşük bir sayı girin")

    if hak == 0:    # En sonunda hak 0 a eşit olursa oyun biter ve alttaki yazı çıkar Ve tahminin doğru cevabını söyler.
        print(f"Hakkınız bitti. Tutulan sayı : {sayi}")