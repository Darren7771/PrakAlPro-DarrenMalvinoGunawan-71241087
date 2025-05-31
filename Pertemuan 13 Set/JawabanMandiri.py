# """Soal no 1"""
# def kategoriAlpikasi():    
#     n = int(input('Masukkan jumlah kategori: '))
#     data_aplikasi = {}
#     for i in range(n):
#         nama_kategori = input('Masukkan nama kategori: ')
#         print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
#         aplikasi = []
#         for j in range(5):
#             nama_aplikasi = input('Nama aplikasi: ')
#             aplikasi.append(nama_aplikasi)
#         data_aplikasi[nama_kategori] = aplikasi
#     daftar_aplikasi_list = []
#     for aplikasi in data_aplikasi.values():
#         daftar_aplikasi_list.append(set(aplikasi))

#     hasil = daftar_aplikasi_list[0]
#     for i in range(1, len(daftar_aplikasi_list)):
#         hasil = hasil.intersection(daftar_aplikasi_list[i])

#     print(hasil)

#     penyimpananAplikasi = {}
#     for daftar in data_aplikasi.values():
#         for app in daftar:
#             if app in penyimpananAplikasi:
#                 penyimpananAplikasi[app] += 1
#             else:
#                 penyimpananAplikasi[app] = 1

#     print("\n== APLIKASI YANG HANYA MUNCUL DI 1 KATEGORI ==")
#     a = 1
#     for app in penyimpananAplikasi:
#         if penyimpananAplikasi[app] == 1:
#             print(f"{a}. {app}")
#             a += 1
#     if n >= 2:
#         print("\n== APLIKASI YANG MEMILIKI 2 KATEGORI ==")
#         b = 1
#         for app in penyimpananAplikasi:
#             if penyimpananAplikasi[app] == 2:
#                 print(f"{b}. {app}")
#                 b += 1
# kategoriAlpikasi()

# """Soal no 2"""
# def list_jadi_set():
#     list_nama = ["Darren","Malvino","Doni","Peter"]
#     setUntukList = set(list_nama)
#     print(f"\nList : {list_nama}")
#     print("List Diatas Menjadi Set : ",setUntukList)

# """SET MENJADI LIST"""
# def set_jadi_list():
#     set_angka = {1,2,3,4,5}
#     listUntukSet = list(set_angka)
#     print("\nSet Awal:",set_angka)
#     print("Set Menjadi List: ",listUntukSet)

# """Tuple Menjadi Set"""
# def tuple_jadi_set():
#     tuple_awal = ("Donnaruma","Peter Cech","Manuel Neuer")
#     setUntukTuple = set(tuple_awal)
#     print("\nTuple Awal :", tuple_awal)
#     print("Tuple menjadi Set :",setUntukTuple)

# """Set menjadi Tuple"""
# def set_jadi_tuple():
#     set_nilai = (100,87,99,77,33)
#     tupleUntukSet = tuple(set_nilai)
#     print("\nSet awal : ", set_nilai)
#     print("Set menjadi Tuple :",tupleUntukSet)

# list_jadi_set()
# set_jadi_list()
# tuple_jadi_set()
# set_jadi_tuple()

"""Soal no 3"""
def fileIsiSama():
    while True:
        try:
            filePertama = input("Masukkan Nama File Pertama: ")
            fileKedua = input("Masukkan Nama File Kedua : ")
        
            with open(filePertama,"r")as file:
                    data1 = file.read().lower().split()
            with open(fileKedua,"r")as file:
                    data2 = file.read().lower().split()
            SetData1 = set(data1)
            SetData2 = set(data2)    
            Sama = SetData1 & SetData2

            print("Berikut adalah Kata yang muncul berulang kali:")
            a = 1
            for kata in Sama:
                print(f"{a}. {kata}")
                a += 1
            break
        except:
            print("Tolong Masukkan Nama File yang benar!")
           
fileIsiSama()