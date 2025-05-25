"""Soal no 1"""
def trueFalse(tA):
    sama = True
    for i in tA:
        if i is not tA[0]:
            sama = False 
    print(sama)
trueFalse(tA= (90, 90, 90, 90))
trueFalse(tA= (90, 20, 22, 33))
trueFalse(tA= (90, 90, 90, 88))

"""Soal no 2"""
def dataDiri(data):
    nama, nim, alamat = data
    
    nimPisah2 = tuple(nim)
    namaAwal = nama.split()[0]  
    nama_depan_pisah2 = tuple(namaAwal)
    namaKebalik = tuple(reversed(nama.split()))

    print("Data :",data)
    print("\nNIM :", nim)
    print("NAMA :", nama)
    print("ALAMAT :", alamat)
    print("\nNIM:", nimPisah2)
    print("\nNAMA DEPAN:", nama_depan_pisah2)
    print("\nNAMA TERBALIK:", namaKebalik)


dataDiri(data = ( 'Murphy Salamanca', '71241099', 'Alburquerque, Spanyol'))

"""Soal no 3"""
def distribusiJam():
    while True:
        try:
            nama_file = input("Enter a file name: ")
            file = open(nama_file)
            break
        except:
            print("Anda Salah memasukkan File! Masukkan file dengan benar!")
    simpan_jam_email = {}
    for baris in file:
        if baris.startswith("From "):
            pisahBaris = baris.split()
            waktu = pisahBaris[5]
            jam = waktu.split(':')[0]
            if jam not in simpan_jam_email:
                simpan_jam_email[jam] = 1
            else: 
                simpan_jam_email[jam] += 1
    for jam in sorted(simpan_jam_email):
        print(jam, simpan_jam_email[jam])
distribusiJam()
