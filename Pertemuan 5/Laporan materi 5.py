nama = str(input("Masukkan Nama anda : "))
umur = int(input("Masukkan Umur anda : "))
tinggi = int(input("Masukkan tinggi anda :"))

print(f">> Hai {(nama)}\n>> umur : {(umur)}\n>> Tinggi anda adalah : {(tinggi)} cm")

def MenghitungLuasPersegi(P,L):
    hasil = P*L
    return hasil
kesimpulan = MenghitungLuasPersegi(10 , 5)
print(kesimpulan)


def Menghasilkan3Kali(Angka):
    print(Angka)
    print(Angka)
    print(Angka)

print(Menghasilkan3Kali(10*10))

def Menghasilkan3Kali(Angka):
    print(Angka)
    print(Angka)
    print(Angka)

Menghasilkan3Kali(10*10)

def perkalian(Angka1,Angka2):
    Hasil = Angka1 * Angka2
    
    return Hasil

nilai1 = 100
nilai2 = 9

Luas = perkalian(nilai1, nilai2)
print(Luas)

def bayarparkir (parkir ,perjam=0):
    bayar =parkir * perjam
    return bayar 
print(bayarparkir(5000))
print(bayarparkir(5000,10))
print(bayarparkir(5000,24))

def Memanggil(nama1,nama2,nama3,nama4):
    print("Orang Pertama:",nama1)
    print("Orang Kedua:",nama2)
    print("Orang Ketiga:",nama3)
    print("Orang Keempat:",nama4)

Memanggil(nama1="Darren", nama2="Doni",nama3="pekimal",nama4 = "totok")

def kelilinglingkaran(pi,d):
    hasil = pi * d 
    return hasil
print(kelilinglingkaran(3.14,30))

kelilinglingkaran = lambda pi,b : pi*b
print(kelilinglingkaran(3.14,30))

membalikan_string = lambda s: s[::-1]

print(membalikan_string("hello")) 
print(membalikan_string("Kamu"))
print(membalikan_string("lala"))
print(membalikan_string("apa"))   

genap_ganjil = lambda x: "Genap" if x % 2 == 0 else "Ganjil"

print(genap_ganjil(9))  
print(genap_ganjil(203))  
print(genap_ganjil(7))  
print(genap_ganjil(2)) 
print(genap_ganjil(5))   



