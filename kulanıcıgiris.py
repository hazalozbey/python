#kullanıcı programı(kullanıcıadı,kullanıcıparolası,girişhakkı)
kullanıcı_adı="hazal"
kullanıcı_parola="hazal.1998"
giris_hakkı=3
while True:
    gkullanıcıadı=input("kullanıcı adı giriniz:") 
    gparola=input("parola giriniz") 
    if (gkullanıcıadı!=kullanıcı_adı and gparola==kullanıcı_parola):
            print("kullanıcı bulanamadı") 
            giris_hakkı-=1
    elif (gkullanıcıadı==kullanıcı_adı and gparola!=kullanıcı_parola):
            print("parola hatalı")
            giris_hakkı-=1
    elif (gkullanıcıadı!=kullanıcı_adı and gparola!=kullanıcı_parola):
            print("hatalı bilgiler")
            giris_hakkı-=1
    else:
        print("sisteme giriş yapılıyor")            
    if (giris_hakkı==0):
            print("giriş hakkınız kalmadı")
            break     
     