#def selamla():
#    print("merhaba")
#     print("nasılsınız")
# print(selamla())
# def selamla1(isim):
#    print("isminiz:",isim)
# print(selamla1("hazal"))
#def toplama(a,b,c):
#    print("toplamları",a+b+c)
#print(toplama(1,2,3))
#def faktöriyel(sayi):
#    faktöriyel=1
#   if(sayi==0 or sayi==1):
#        print("faktöriyel",faktöriyel)
#    else:
#        while(sayi>=1):
#            faktöriyel *=sayi
#           sayi -=1
#            print("faktöriyel",faktöriyel)
#print(faktöriyel(1))
#def toplama(a,b,c):
#    return a+b+c
#def ikiylecarp(a):
#   return a*2
#toplam=toplama(2,3,4)
#print(ikiylecarp(toplam))
def ücleçarp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a+2
def dördeböl(a):
    print("3.fonksiyon çalıştı")
    return a/4
print(dördeböl(ikiyletopla(ücleçarp(5))))