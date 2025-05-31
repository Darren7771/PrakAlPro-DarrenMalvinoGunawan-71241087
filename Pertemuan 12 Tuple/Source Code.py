buah = ("pisang", "apel", "alpukat")
angka = 1,2,3 
angka2 = (1,2,3)
print (buah) 
print (angka) 
print (type(angka2)) 

tupleKosong = tuple()
nilai = (70,88,99)
# nilai[0] = 70
nilai = (73,) + nilai[1:]
print(nilai)
print(nilai[1])

print((1,3,4)<(2,1,0)) 

kalimat = "hai halo namaku darren"
daftar_kata = kalimat.split()

urutan_kata = []
for kata in daftar_kata:
    urutan_kata.append((len(kata), kata))

urutan_kata.sort(reverse=True)
hasil = []
for panjang, kata in urutan_kata:
    hasil.append(kata)

print(hasil)

nama = ("Vino", "Victoria","Palito")
depan,tengah,belakang = nama
print(depan,tengah,belakang)

angka= (1,2)
satu,dua =angka
print(satu,dua)

baru = (3,4,5)
tiga,empat = baru
print(tiga,empat)

a,b = "aku","kamu"
a,b = b,a
print(a,b)

absen = {"aaron" : 1, "bonita" : 2, "cello" : 3}
items = list(absen.items())
a = 0 
for i in items:
    print(items[a])
    a += 1

harga = { 'rokok': 50, 'korek' : 2,'kopi': 20}
item = list(harga.items())
item.sort()
print(item)

penjualan = {'permen': 6, 'chiki' : 10, 'sabun' : 5}
angka = 1 
for key, value in penjualan.items(): 
    print(f"{angka}.{key} => {value} items")
    angka += 1


file = open("File.txt")
frekuensi = {}

for baris in file:
    kata_kata = baris.split()
    for kata in kata_kata:
        kata = kata.lower()  
        if kata in frekuensi:
            frekuensi[kata] += 1
        else:
            frekuensi[kata] = 1
daftar = []
for kata, jumlah in frekuensi.items():
    daftar.append((jumlah, kata))
daftar.sort(reverse=True)

for jumlah, kata in daftar:
    print(f"{kata} : {jumlah}")

nilai = {}

nilai[("budiono","nyeni","speed")] = 80
nilai[("todo","maruli","pasaribu")] = 90
for (depan,belakang,tengah) in nilai:
    print(depan,tengah,belakang,nilai[(depan,belakang,tengah)])