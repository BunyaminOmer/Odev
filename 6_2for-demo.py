sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesindeki hangi sayılar 3'ün katıdır ?

for sayi in sayilar:
    if print(sayi%3==0):
        print(sayi)

# 2- Sayılar listesinde sayıların toplamı kaçtır ?

toplam = 0 
for sayi in sayilar:
    toplam += sayi
    print("toplam:",toplam)

# 3- Sayılar listesindeki tek sayıların karesini alınız.

for sayi in sayilar:
    if (sayi % 2 == 1):
        print(sayi ** 2)

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"] 

for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir)

urunler = [
    {"name":"Samsung S6", "price": "3000"},
    {"name":"Samsung S7", "price": "4000"},
    {"name":"Samsung S8", "price": "5000"},
    {"name":"Samsung S9", "price": "6000"},
    {"name":"Samsung S10", "price": "7000"}
]

# 5- Ürünlerin fiyatlarının toplamı nedir?

toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])
    toplam += fiyat
print("toplam ürün fiyatı: ", toplam)

#  6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for urun in urunler:
    if (int(urun["price"]) <= 5000):
        print(urun["name"])