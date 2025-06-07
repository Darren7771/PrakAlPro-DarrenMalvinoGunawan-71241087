# def namaFungsi(parameter):
#     if baseCase : 
#         return (nilaiAkhir)
#     else:
#         return namaFungsi(parameterBaru)



# def pangkat(angka, pangkat_dari_angka): 
#     if pangkat_dari_angka == 0:
#         return 1 
#     else: 
#         return angka * pangkat(angka,pangkat_dari_angka-1)
# hasil = pangkat(8,3)
# print("hasil nya :",hasil)

     

# def Faktorial(angka):
#     if angka == 0 or angka == 1: 
#         return 1
#     else : 
#         return angka * Faktorial(angka-1) 

# # hasil = Faktorial(5)
# # print(hasil)

# def faktorial(n):
#     hasil = 1
#     for i in range(1, n+1):
#         hasil *= i
#     return hasil

# print(faktorial(5)) 

def fibo (angka):
    if angka <= 1: 
        return angka
    else :
        return fibo(angka - 1) + fibo(angka - 2)
    
def fibo (angka): 
    pertambahan, pertambahan2 = 0,1
    for i in range(angka):
        pertambahan,pertambahan2 = pertambahan2, pertambahan + pertambahan2
    return pertambahan 
print(fibo(6))

        
    


     
