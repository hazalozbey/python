'''
#open("deneme.txt","w")dosya yoksa oluşturur varsa silip tekrar oluşturuyor
file=open("deneme.txt","w",encoding="utf-8")
file.write("hazal özbey")
file.close()#dosyayı kapatma
file=open("deneme.txt","a",encoding="utf-8")#olan dosyayı açar
file.close()
file=open("yapayzeka.txt","r",encoding="utf-8")#dosyayı okuma ve yazdırma
for i in file:
    print(i)
file.close()
file=open("yapayzeka.txt","r",encoding="utf-8")
icerik=file.read()#dosya yazdırmada farklı kullanım
print(icerik)
file.close()

file=open("yapayzeka.txt","r",encoding="utf-8")
print(file.readline())#dosyanın ilk satırını okumak için 
file.close()

file=open("yapayzeka.txt","r",encoding="utf-8")
liste=file.readlines()#liste tipinde okumak için
print(liste)

#ya kapatmanın unutulması durumu için yapılan işlemlerden sonra dosyayı
#kapatan yapı
with open("yapayzeka.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i)

with open("yapayzeka.txt","r",encoding="utf-8") as file:
    print(file.tell())#dosya imlecinin hangi indiste olduğunu döndüren fonk.
    file.seek(20)
    print(file.tell())

with open("yapayzeka.txt","r",encoding="utf-8") as file:
    file.seek(5)
    icerik=file.read(10)
    print(icerik)

with open("deneme.txt","a",encoding="utf-8") as file:
    file.write("öğrenci\n")

with open("deneme.txt","a",encoding="utf-8") as file:
    icerik=file.read()
    icerik="öğrenci\n" + icerik
    file.seek(0)
    file.write(icerik)

with open("deneme.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(3,"pyhon\n")
    file.seek(0)
    for i in liste:
        file.write(i)
with open("deneme.txt","r+",encoding="utf-8") as file:
    dosya=file.read()
    print(dosya)
'''
with open("deneme.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(3,"java\n")
    file.seek(0)
    file.writelines(liste)
with open("deneme.txt","r+",encoding="utf-8") as file:
    dosya=file.read()
    print(dosya)





















