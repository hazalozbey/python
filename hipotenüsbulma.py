#kullanıcıdan bir üçgenin dik ola iki kenarını (a,b) alın ve hipotenüsü bulun

a=int(input("a kenarını uzunluğunu giriniz:"))
b=int(input("b kenarının uzunluğunu giriniz:"))
hip=sqrt((a**2)+(b**2))
print("hipotenüs:{}".format(hip))