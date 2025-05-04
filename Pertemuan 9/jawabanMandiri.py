# """Jawaban soal no 1"""
# def pembanding (file2022,file2023):
#     with open(file2022 + ".txt","r") as filePertama:
#         data2022 = filePertama.readlines() 
#     with open(file2023 + ".txt","r") as fileKedua:
#         data2023 = fileKedua.readlines() 

#     panjang = max(len(data2022),len(data2023))
#     panjangData2022 = len(data2022)
#     panjangData2023 = len(data2023)
    
#     data2022.extend([""] * (panjang - panjangData2022))
#     data2022.extend([""] * (panjang - panjangData2023))


#     for i in range(panjang):
#         baris2022 = data2022[i].strip()
#         baris2023 = data2023[i].strip()

#         if baris2022 == baris2023:
#             print(f'Pada baris ke-{i+1} sama :')
#             print(f'* Produk Handphone 2022 \n>',baris2022)
#             print(f'* Produk Handphone 2023 \n>',baris2023)

#         else:
#             print(f'Pada baris ke-{i+1} berbeda :')
#             print(f'* Produk Handphone 2022 \n>',baris2022)
#             print(f'* Produk Handphone 2023 \n>',baris2023)            
            
# pembanding("produkHandphone2022", "produkHandphone2023")

"""Jawaban soal no 2"""
def jawabSoal(file):
    with open(file+".txt","r") as files:
        dataSoal  = files.readlines()
        print("nama file1:",files.name)
        
        soal = [baris.split("||") for baris in dataSoal]
        
        for i in soal:
            print(i[0].strip())
            inputJawaban = input("Jawab: ")
            jawabanAsli = i[1].strip()
            if inputJawaban == jawabanAsli:
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")
            
jawabSoal("soal")
