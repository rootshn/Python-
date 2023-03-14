print("Hello mr.Rootshn, welcome to your first code")

#veri tipleri 

baslik = "Tasit Kredisi"
print(baslik)
#string = metinsel ifade
baslik = "ihtiyac kredisi"
print(baslik)

#int, integer = tam sayi
vade = 36
ekVade = 6
vade2 = "36"

# float, double
aylikOdeme = 200.50

# bool, boolean = True or False 
yükselisteMi = False

# matematiksel operatorler
# .
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)
# .
print(5-5)
print(vade-12)
print(vade - ekVade)
print(36-6)

# *
print(55)
print(vade2)

# /
print(5/5)
print(vade/2)

yeniVade = vade / 2
fiyat = 100 
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % = mod operator
print(10%2)
print(vade % 3)
print(30 % 10)

# mantiksal oparatorler
print(1 == 1)
print(2 == 1)

print(3 > 2)
print(2 > 3)
print(1 >= 1)

print(1 < 2)
print(2 < 3)
print(2 < 1)
print(1 != 1)

# or and

#or => veya 
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)
print(True and True)
print(False | False)

#Decide Blocks
#if else
sayi1=10
sayi2=10
#Compare it, is sayi1 > sayi2?

#indent
if sayi1 > sayi2:#conditions(şart)
    print("Sayi1 bigger than Sayi2")
    print("I'm still in if block")
print("Now we are in out of if block")
print("********************")

if sayi1<sayi2:
    print("Sayi1 smaller then Sayi2")
elif sayi1>sayi2:
    print("Sayi1 bigger then Sayi2")
else:
    print("Sayi1 and Sayi2 are equals")
