
#bir aracın kilometrede ne kadar yaktığını ve kaç km yol aldığı bilgilerine göre 
#ne kadar ödemesi gerektiğini hesaplayın

yakıtfiyatı=int(input("aracınız kilometre başına ne kadar benzin harcar"))
yol=int(input("kaç km yol gittiniz:"))
tutar=yakıtfiyatı*yol
print("ödeyeceğiniz tutar {}".format(tutar))