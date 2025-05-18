# dictionaryKosong = dict()
# print(dictionaryKosong) # outputnya {}

# dictionaryKosong ['nama'] = 'eko'
# print(dictionaryKosong)

# listKosong = list()
# print(listKosong) # Outputnya []

# karyawan = {
#     "nama" : 'Danu',
#     "umur" : '32',
#     'gelar' : 'S1 dan S2',
#     'bidang' : 'animasi'  
# }
# print(karyawan['gelar'])

# karyawan = {"nama" : 'Danu',"umur" : '32','gelar' : 'S1 dan S2','bidang' : 'animasi'  }


# kata = 'aku pergi ke kantor bapak'
# counter = {}

# for i in kata:
#     if i in counter:
#         counter[i] += 1 
#     else:
#         counter[i] = 1 
# print(counter)


# nilai = {
# "Darren" : 98,
# "Peter" : 88,
# "dodo" : 97
# }
# print(nilai.get('Darren' , 0))
# print(nilai.get('toronto', 98))



# file = input(str("Masukkan nama file: "))
# try:
#     with open(file) as berkas:
#         hitung_kata = {}

#         for baris in berkas:
#             kata_per_baris = baris.split()
#             for kata in kata_per_baris:
#                 if kata in hitung_kata:
#                     hitung_kata[kata] += 1
#                 else:
#                     hitung_kata[kata] = 1

#         print(hitung_kata)

# except :
#     print("File Salah!!")
#     exit()

# vokal = "iaueo"
# hitungVokal = {}

# with open("cerita.txt","r") as file:
#         for baris in file:
#             baris = baris.lower()  
#             for huruf in baris:
#                 if huruf in vokal:
#                     if huruf in hitungVokal:
#                         hitungVokal[huruf] += 1
#                     else:
#                         hitungVokal[huruf] = 1

# print("Jumlah kemunculan huruf vokal:")
# for huruf in vokal:
#     if huruf in hitungVokal:
#         print(f"{huruf} : {hitungVokal[huruf]}")

tinggiCm = {'Rina': 165, 'Kim': 176, 'Pietro':188,'Nella':170}
# valueTinggi = list (tinggiCm.values()) 
# keyTinggi = list(tinggiCm.keys())
# valueTinggi.sort()
# print(valueTinggi)
# keyTinggi.reverse()
# print(keyTinggi)
# for i in tinggiCm:
#     print(i,tinggiCm[i])

for i in tinggiCm.values():
    print(i)
for j in tinggiCm.keys():
    print(j)

import string
nama_file = input("Masukkan nama file: ")
with open(nama_file) as file:
    data = {}
    for baris in file:
        baris = baris.translate(str.maketrans('', '', string.punctuation))
        baris = baris.lower()
        kata = baris.split()
        for k in kata:
            if k in data:
                data[k] += 1
            else:
                data[k] = 1

print("Hasil perhitungan kata:")
print(data)