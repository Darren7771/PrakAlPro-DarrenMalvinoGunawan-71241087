# """Jawaban No 3"""
# def pesanGmail ():
#     while True:
#         try:
#             nama_file = input("Masukkan nama file: ")
#             file = open(nama_file)
#             break
#         except:
#             print("Anda Salah memasukkan File! Masukkan file dengan benar!")
#     data_email = {} 
#     for baris in file:
#         if baris.startswith('From '):
#             pisah = baris.split()
#             email = pisah[1]
#             if email in data_email:
#                 data_email[email] += 1
#             elif email not in data_email:
#                 data_email[email] = 1 
#     print(data_email)

# pesanGmail()

# """Jawaban no 4"""
# def domainPengirimPesan ():
#     while True:
#         try:
#             nama_file = input("Masukkan nama file: ")
#             file = open(nama_file)
#             break
#         except:
#             print("Anda Salah memasukkan File! Masukkan file dengan benar!")
#     dataDomain = {} 
#     for baris in file:
#         if baris.startswith('From '):
#             pisah = baris.split()
#             email = pisah[1]
#             domain = email.split('@')[1]
#             if domain in dataDomain:
#                 dataDomain[domain] += 1
#             else:
#                 dataDomain[domain] = 1 
#     print(dataDomain)

# domainPengirimPesan()