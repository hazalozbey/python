from math import *
import cmath 
#Basit bir oyucu kaydetme programı
'''
isim=input("isimizi giriniz:")
soyisim=input("soyisim giriniz:")
parola=input("parola giriniz:")
print("kullanıcı ismi:{}\n kullanıcı soyadı:{}\n parolası:{}\n".format(isim,soyisim,parola))
'''
#kökler toplamı ve kökleri bulma
'''
a=int(input("a sayısını giriniz:"))
b=int(input("b sayısını giriniz:"))
c=int(input("c sayısını bulunuz:"))
delta=(b**2-(4*a*c))
print(delta)
x1=((-b+(sqrt(delta)))/(2*a))
x2 =((-b-(sqrt(delta)))/(2*a))
print("birinci kök: {} \n ikinci kök :{}".format(x1,x2))
'''
#kullanıcıdan alınan boy ve kilo ie vücut indexi hesaplayıp hangi aralıkta olduğunu göster
'''
boy=int(input("boyunuzu giriniz"))
boy=boy/100
kilo = int(input("kilonuzu giriniz"))
vucütindexi=kilo/(boy**2)
if vucütindexi<18.5:
    print("zayıf")
elif vucütindexi < 25 and vucütindexi>18.5:
    print("normal")
elif vucütindexi < 30 and vucütindexi>25:
    print("kilolu")
elif vucütindexi>30:
    print("obez")
else:
    print("yanlış giden birşeyler oldu")
'''
#bir aracın kilometrede ne kadar yaktığını ve kaç km yol aldığı bilgilerine göre 
#ne kadar ödemesi gerektiğini hesaplayın
'''
yakıtfiyatı=int(input("aracınız kilometre başına ne kadar benzin harcar"))
yol=int(input("kaç km yol gittiniz:"))
tutar=yakıtfiyatı*yol
print("ödeyeceğiniz tutar {}".format(tutar))
'''
#kullanıcıdan iki sayı al ve değerlerini kendi aralarında değiştir
'''
sayi1=input("birinci sayiyi giriniz:")
sayi2=input("ikinci sayiyi giriniz:")
sayi1, sayi2 = sayi2, sayi1
print("sayi1 =", sayi1)
print("sayi2 =", sayi2)
'''
#kullanıcıdan bir üçgenin dik ola iki kenarını (a,b) alın ve hipotenüsü bulun
'''
a=int(input("a kenarını uzunluğunu giriniz:"))
b=int(input("b kenarının uzunluğunu giriniz:"))
hip=sqrt((a**2)+(b**2))
print("hipotenüs:{}".format(hip))
'''
#Basit Hesap Makinesi
print("")