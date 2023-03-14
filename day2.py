faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade)+12)

faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
vade = vade + 12


#string interpolation
# seçtiğiniz vade sonucu ortaya çıkan vade
print("Seçtiğini vade sonucu ortaya çıkan: " + str(vade))
print("Seçtiğiniz vade sonucu çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")
isim = "Berkay" #input("isminizi giriniz")
metin = "Merhaba {name}".format(name=isim)
print(metin)


# f-string 
metin = f"Hoşgeldiniz {isim}"
print((metin))

#arrays/collections/lists

krediler=["İhtiyaç kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))
print(krediler[0])

print(len(krediler))
print(krediler[2])

#print(krediler[3]) => out of index hatası verir. 

dizi= ["İhtiyaç Kredisi", 10 , 5.2, True]
print(dizi)

#listenin sonuna ekleme yapmak için özel bir fonksiyonumuz var 
krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop() # default olarak son elemanı siler eğer index verirsen verdiğin indexi siler.
print(krediler)
krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")# Bir taşıt kredisi daha ekleyelim..
krediler.remove("Taşıt Kredisi")# Bulduğu ilk elemanı siler
print(krediler)

krediler.extend(["y Kredisi", "Z Kredisi"])
print(krediler)

#Loops

#for
#i = 0 i<10

for i in range(10):
    print("xx")
    print(i)
print("*****************")
for i in range(5,10):
    print(i)
print("**************")
for i in range(2,21,5):
    print(i)
# for i in range(0.1,0.5): TypeError: 'float' object cannot be interpreted as an integer.
#     print(i)

print("**************")
 
krediler=["İhtiyaç kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("**************")
for i in range(len(krediler)):
    print(krediler)
print("**************")

i = 0
while i < 10:
    print("x")
    i+= 1
print("y")
print("************")

while True: #while döngüsünü bitirme
    print("x")
    break
print("************")
i = 0
while i < len(krediler):

    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i+= 1

#methods/functions

fiyat = 100
indirim = 20
# definition define

def calculate():
    print(100-20)
    
def calculateWithParam(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParam(50,10)
calculateWithParam(100,30)
sayHello("Berkay")


def calculateAndReturn(price, discount):
    return price-discount

newPrice = calculateAndReturn(200,50)
print(newPrice)