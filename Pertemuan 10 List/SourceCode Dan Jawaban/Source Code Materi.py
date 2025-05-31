list1 = [1,3,4,2,94.4,5.2,56,7.6,8,5,4.3] #Int dan Float
list2 = ["kata1","kata2","kata3","kata4","kata5"] # integer
list3 = ["ayam", 2, 3.4, True, False, [1, 3.4, "katakata"]] #Campuran serta list dalam list

print(list1)
print(list2)
print(list3)


tas = ["dompet","buku", "alat tulis","botol minum"]
print(tas[1]) 


kelasAwal = ["budi","edi","lalo"] 
kelasAwal[0] = "sisil"
print (kelasAwal) # nanti dilist kelasAwal kata budi akan di ganti dengan sisil
print(kelasAwal[0:2]) 

print(kelasAwal[2:0])

muridLama = ['andi','doni','salamanca','walter', 'putri']
muridBaru = ['gustavo','mike','van']
total_murid = muridLama + muridBaru
list2 = muridLama * 2
print(total_murid)
print (list2)

# handphone = ["samsung","iphone","xiaomi"]
# handphone.append("oppo")
# print(handphone)

kode1 = [27392 , 3829328, 3383823, 383922]
kode1.append([27392 , 3829328, 3383823, 383922])
print(kode1)

makanan = ['mie','ayam goreng','tahu goreng']
makanan.insert(2,"tempe")
print(makanan)

minuman = ["es teh", "air", 'es jeruk']
minuman.pop(1)
print(minuman)

soda = ['sprite', 'coca cola','fanta']
soda.pop()
print(soda)

bagasi = ['ban','perkakas','remote tv']
bagasi.remove('remote tv')
print(bagasi)

angka = [1,2,3,2,4,2,5]
angka.remove(2)
print (angka)

box = ['bola merah','bola kuning']
del box[1]
print (box)

urutAbsen = ['celi','bimo','adrian']
Angka = [7,5,4,3,7,5,3,7,8]
urutAbsen.sort()
Angka.sort()
print(urutAbsen)
print(Angka)

kode = [132,233,322,423,542,612,732    ]
kode.reverse()
print(kode)

nilaiUlangan = [100,87,66,89,44,65,66]
maks = max(nilaiUlangan)
min= min(nilaiUlangan)
sum= sum(nilaiUlangan)
len = len(nilaiUlangan)
print(f"Maks :{maks}")
print(f"Min : {min}")
print(f"Sum : {sum}")
print(f"Len : {len}")

angka = [1,2,3,4,5]
angkaGenap = [x for x in angka if x%2 == 0]
print(angkaGenap)

negara = ['Colombia','Mexico','Texas']
panjangKata = [len(x)for x in negara]
print(panjangKata)

def tanpaDuplikat (data):
    return list(set(data))
print(tanpaDuplikat([1,2,3,3,3,3,3,4,4])) #test case

mobil = ['porsche','audi','bentley','mazda']
lebih_dari_4_kata = [x for x in mobil if len(x)>4]
print(lebih_dari_4_kata)

def panjangKata (mobil):
    return [x for x in mobil if len(x)>4]
print(panjangKata(['porsche','audi','bentley','mazda']))