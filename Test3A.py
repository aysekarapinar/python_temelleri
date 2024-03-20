#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

boy=float(input("Boyunuzu metre cinsinden giriniz : "))
agirlik =float(input("ağırlığınızı kilogram cinsinden giriniz "))
VKI= agirlik/(boy*boy)
print ("vücut kitle indeksiniz:",VKI )

#2.soru
maas=float(input("Mevcut maaşı girin :"))
zam_orani=float(input("Zam  oranını yüzde olarak  giriniz :"))

yeni_maas=((maas/100)*zam_orani)+maas
print(yeni_maas)

#3.soru
sayi1=float(input("1.sayiyi giriniz"))
sayi2=float(input("2.sayiyi giriniz"))
sayi3=float(input("3.sayiyi giriniz"))

en_buyuk = sayi1

if sayi2 > en_buyuk:
    en_buyuk = sayi2

if sayi3 > en_buyuk:
    en_buyuk = sayi3
print("En büyük sayı:", en_buyuk)

#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
yari_cap=float(input("daire'nin yarıçapını giriniz!"))
pi=3.14
alan=pi*yari_cap*yari_cap
cevre=pi*(yari_cap+yari_cap)
print("daire'nin çevresi:",cevre)
print ("daire'nin alanı",alan) 

#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = input("Bir sayı girin: ")
ters_sayi = sayi[::-1]
if sayi == ters_sayi:
    print("Girilen sayı bir palindromdur.")
else:
    print("Girilen sayı bir palindrom değildir.")