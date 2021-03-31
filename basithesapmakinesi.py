print("Hesap makinesi açıldı")
print("Toplama işlemi yapmak için '+' tuşuna basın")
print("Çıkarma işlemi yapmak için '-' tuşuna basın")
print("Bölme işlemi yapmak için '/' tuşuna basın")
print("Çarpma işlemi yapmak için '*' tuşuna basın")
giris=input("işlem giriniz:")
sayı1=int(input("Birinci sayıyı giriniz:"))
sayı2=int(input("ikinci sayıyı giriniz:"))
if giris=='+':
    print("toplama işlemi yapılıyor")
    print("Sonuç" , (sayı1+sayı2))
elif giris=='-':
    print("Çıkarma işlemi yapılıyor")
    print("Sonuç"(sayı1-sayı2))
elif giris=='/':
    print("Bölme işlemi yapılıyor")
    print("Sonuç"+(sayı1/sayı2))
elif giris=='*':
    print("Çarpma işlemi yapılıyor")
    print("Sonuç"+(sayı1*sayı2))
else:
    print("geçersiz işlem")



