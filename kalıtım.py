class Calisan:
    def __init__(self,isim,maas,departman):
        print("çalışan sınıfının init fonksiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgilerigöster(self):
        print("çalışan sınıfının bilgileri")
        print("isim: {} \n maaş: {} \n departman:{}\n".format(self.isim,self.maas,self.departman))
    def departman_degistir(self,yeni_departman):
        self.departman=yeni_departman

'''class Yönetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayısı):
        print("yönetici sınıfının init fonksiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman
        self.kisi_sayısı=kisi_sayısı
    def zamYap(self,zam_miktari):
        self.maas+=zam_miktari

    def bilgilerigöster(self):
        print("yönetici sınıfının bilgileri")
        print("isim: {} \n maaş: {} \n departman:{}\n kişi sayısı:{}\n".format(
            self.isim, self.maas, self.departman,self.kisi_sayısı))
'''


class Yönetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayısı):
        print("yönetici sınıfının init fonksiyonu")
        super().__init__(isim,maas,departman)
        self.kisi_sayısı = kisi_sayısı

    def zamYap(self, zam_miktari):
        self.maas += zam_miktari

    def bilgilerigöster(self):
        print("yönetici sınıfının bilgileri")
        print("isim: {} \n maaş: {} \n departman:{}\n kişi sayısı:{}\n".format(
            self.isim, self.maas, self.departman, self.kisi_sayısı))
yönetici=Yönetici("hazal",3500,"bilişim",10)
#yönetici.departman_degistir("insan kaynakları")
yönetici.bilgilerigöster()
