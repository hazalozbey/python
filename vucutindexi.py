#kullanıcıdan alınan boy ve kilo ie vücut indexi hesaplayıp hangi aralıkta olduğunu göster

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
