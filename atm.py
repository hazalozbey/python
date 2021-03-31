print("""******************
Atm makinesine hoş geldiniz
işlemler
1-Bakiye Sorgulama
2-Para Yatırma
3-Para Çekme

programdan çıkmak için 'q' basın.

**********""")
bakiye=1000
while True:
    islem=input("işlemi seçiniz: ")
    if(islem=='q'):
        print("yine bekleriz")
        break
    elif(islem=="1"):
        print("bakiyeniz {} tldir".format(bakiye))
    elif(islem=="2"):
        miktar=int(input("Miktarı giriniz:"))
        bakiye+=miktar
    elif(islem=="3"):
        miktar = int(input("Miktarı giriniz:"))
        
        if(bakiye-miktar<0):
            print("bakiye yetersiz")
            continue
        bakiye -= miktar
    else:
        print("geçersiz işlem")
