#kullanıcıdan iki sayı al ve değerlerini kendi aralarında değiştir

sayi1=input("birinci sayiyi giriniz:")
sayi2=input("ikinci sayiyi giriniz:")
sayi1, sayi2 = sayi2, sayi1
print("sayi1 =", sayi1)
print("sayi2 =", sayi2)