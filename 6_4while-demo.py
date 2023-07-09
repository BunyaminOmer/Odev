sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesini while ile ekrana yazdırın.

i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.

baslangic = int(input("başlangıç : "))
bitis = int(input("Bitiş : "))

i = baslangic
while i < bitis:            # ( i = Başlangıç )  başlangıç bitişten yüksek oluncaya kadar devam eder.
    i += 1                  # Sürekli bir tane daha ekler
    if (i % 2 == 1):        # Eğer tam bölündüğünde modu 1 e eşit gelirse yazdırır yani sadece tek sayılar yazar.
        print(i)

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

i = 100
while i > 0:   # Burada while döngüsü 100 den büyükse yazdırır.
    print(i)   # sürekli yazar ama
    i -= 1     # Sürekli bir sayı eksiltir.

# 4- Kullanıcıdan alacağımız 5 bilgiyi sıralı bir şekilde ekrana yazdırın.

numbers = []

i = 0

while i < 5:
    sayi = int(input("Sayı : "))
    numbers.append(sayi)
    i += 1

numbers.sort()

print(numbers)

# 5- Kullanıcıdan alacağınız ürün bilgisini urunler listesi içinde saklayınız
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name,price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyin.

urunler = []

adet = int(input("Kaç ürün eklemek istiyorsunuz : "))
i = 0

while(i<adet):
    name = input("ürün ismi : ")     # inputta ürün ismi ve ürün fiyatı ister.
    price = input("ürün fiyatı : ")
    urunler.append({
        "name":name,
        "price":price,
    })
    i += 1 # i ye 1 ekleyip eşit oluncaya kadar devam ettiririz.

for urun in urunler:    # for döngüsü ile yazdırırız, az önce yazdığımız ürün ve fiyatları şimdi görürüz.
    print(f"ürün adı: {urun[|"name"|]} ürün fiyatı: {urun["price"]}")


                                                # CLASS IS DISMISSED