#Nama : Rina Sartika
#Nim : D0221067
#kelas : Informatika E

class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi**2

class Segitiga(BangunDatar):
    def __init__(self,alas,tinggi) :
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return self.alas * self.tinggi / 2

class Lingkaran(BangunDatar):
    def __init__(self,jari2):
        self.phi = 22/7
        self.jari2 = jari2

    def luas(self):
        return self.phi * (self.jari2**2)

class BangunRuang:
    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi**3

class Limas(BangunRuang):
    def __init__(self,panjang_alas,tinggi_alas,tinggi_limas):
        self.panjang_alas = panjang_alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_limas = tinggi_limas

    def volume(self):
        return (self.panjang_alas*self.tinggi_alas/2) * self.tinggi_limas / 3

class Tabung(BangunRuang):
    def __init__(self,jari2,tinggi):
        self.phi = 22/7
        self.jari2 = jari2
        self.tinggi = tinggi

    def volume(self):
        return self.phi * (self.jari2**2) * self.tinggi
    
    
def pilihan():
    list = ['1.Bagun Datar','2.Bagun Ruang']
    for i in list:
        print(i)
    masukan = input("Masukan pilihan anda : ")
    if masukan == "1":
        menu_bagundatar()   
    elif masukan == "2":
        menu_bagunruang()
    else:
        print("kode yang anda masukan salah")
        lanjut = input("Lanjut or no (y,n) : ")
        if lanjut == "y" and "Y":
            pilihan()
        elif lanjut == "n" and "N":
            print("program selesai")
            pass

def menu_bagundatar():
    print("MENU BAGUN_DATAR".center (40, ' '))
    daftar = ['1.Persegi','2.Segitiga','3.Lingkaran','4.kembali kemenu','5.Exit']
    for i in daftar:
        print(i)
        
    pilihan = int(input("Masukan pilihan anda : "))
    if pilihan == 1 :
        print("Menghitung luas persegi")
        sisi = int(input("Masukan panjang sisi : "))
        persegi = Persegi(sisi)
        print("luas persegi : ",persegi.luas())
                
    elif pilihan == 2 :
        print("menghitung luas segitiga")
        alas = int(input("masukkan panjang alas segitiga : "))
        tinggi = int(input("masukkan panjang tinggi segitiga : "))
        segitiga = Segitiga(alas,tinggi)
        print("luas segitiga = ",segitiga.luas())
    
    elif pilihan == 3:
        print("menghitung luas lingkaran")
        jari2 = int(input("masukkan panjang jari-jari : "))
        lingkaran = Lingkaran(jari2)
        print("luas lingkaran = ",int(lingkaran.luas()))
    
    elif pilihan == 4 :
        pilihan()
    elif pilihan == 5:
        print("Program selesai")
        pass
    else:
        print('Masukan kode dengan benar!')
        
def menu_bagunruang():
    print("MENU BAGUN RUANG".center(40 , ' '))
    daftar = ['1.Kubus','2.Limas','3.Tabung','4.Kembali ke menu','5.Exit']
    for i in daftar:
        print(i)
    
    pilihan = int(input("Masukan pilihan anda : "))
    if pilihan == 1 : 
        print("menghitung volume kubus")
        sisi = int(input("masukkan panjang sisi : "))
        kubus = Kubus(sisi)
        print("volume kubus = ",kubus.volume()) 
    elif pilihan == 2 : 
        print("menghitung volume limas segitiga")
        alas = int(input("masukkan panjang alas segitiga : "))
        tinggi_alas = int(input("masukkan panjang tinggi alas segitiga : "))
        tinggi_limas = int(input("masukkan panjang tinggi limas : "))
        limas = Limas(alas,tinggi_alas,tinggi_limas)
        print("volume limas segitiga = ",limas.volume())
    elif pilihan == 3 : 
        print("menghitung volume tabung")
        jari2 = int(input("masukkan panjang jari-jari : "))
        tinggi = int(input("masukkan tinggi tabung : "))
        tabung = Tabung(jari2,tinggi)
        print("volume tabung = ",int(tabung.volume()))
    elif pilihan == 4 : 
        pilihan()
    elif pilihan == 5 :
        print('Program selesai')
        pass
    else : 
        print("masukkan kode menu dengan benar!")
