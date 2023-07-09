sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesindeki hangi sayılar 3'ün katıdır ?

for sayi in sayilar:
    if print(sayi%3==0):     # 3'e tam bölünen zaten 3'ün katıdır
        print(sayi)

# 2- Sayılar listesinde sayıların toplamı kaçtır ?

toplam = 0 
for sayi in sayilar:
    toplam += sayi
    print("toplam:",toplam)

# 3- Sayılar listesindeki tek sayıların karesini alınız.

for sayi in sayilar:
    if (sayi % 2 == 1):   # Bu satırda 2 ye tam bölünüp modu 1 e eşitse  sonraki adıma geçer
        print(sayi ** 2)  # Eğer yukarıdaki işlem True ise tek sayıların karesini alır.

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"] 

for sehir in sehirler:
    if (len(sehir) <= 5):    # Şehir içindeki verilerin harf sayısı 5 veya 5 ten küçükse onları ekrana yazdırır.
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
    if (int(urun["price"]) <= 5000):     # 5000 yada 5000 den az para olan ürünleri ekrana yazdırır.
        print(urun["name"])