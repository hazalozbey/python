'''
try:
   
    a=int("234")
    print("program burda")
    
except:
    print("bir hata oluştu")
print("bloklar sona erdi")

try:
    a=int(input("sayi1:"))
    b=int(input("sayi2:"))
    print(a/b)
except ValueError:
    print("lütfen inputu doğru girin")
except ZeroDivisionError:
    print("bir sayi 0'a bölünemez")
finally:
    print("burası çalıştı")
print("bloklar sona erdi")

def terscevir(s):
    if (type(s) != str):
        raise ValueError("lütfen string giriniz:")
    else:
        return s[::-1]
print(terscevir("hazal"))
print(terscevir(1234))

'''
