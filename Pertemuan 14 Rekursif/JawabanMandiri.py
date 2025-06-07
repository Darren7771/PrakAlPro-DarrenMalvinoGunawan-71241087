"""Jawaban no 1"""
def prima(angka, pembagi=2): 
    if angka == 1: 
        return "bukan prima"
    elif pembagi * pembagi > angka: 
        return "bilangan prima" 
    elif angka % pembagi == 0:
        return "bukan prima"
    else: 
        return prima(angka,pembagi + 1)
    
print(prima(67))
print(prima(149))
print(prima(12))
print(prima(10))

"""Jawaban no 2"""
def palindrom(kalimat): 
    kalimat =  ''.join(kalimat.lower().split())
    if kalimat[0] == kalimat[-1]:
        return "Kalimat Palindrom"
    elif kalimat [0] != kalimat[-1]:
        return "Bukan Kalimat Palindrom"
    else: 
        return palindrom(kalimat[1:-1]) 

print(palindrom("Kerang ini retak")) 
print(palindrom("hari ini minggu")) 

"""Jawaban no 3"""
def ganjil(n):
    if n == 1: 
        return 1 
    else:
        return 2 * n - 1 + ganjil(n-1)
print(ganjil(2)) 
print(ganjil(9)) 
print(ganjil(97)) 

"""Jawaban no 4"""
def penjumlahan(angka):
    if angka < 1:
        return 0
    else: 
        return penjumlahan(angka//10) + angka % 10 

print(penjumlahan(0))
print(penjumlahan(99))
print(penjumlahan(234))


"""Jawaban no 5"""
def kombinasi(n,r):
    if n == r or r == 0:
        return 1 
    else:
        return kombinasi(n-1,r) + kombinasi (n-1,r-1)
print(kombinasi(5,2))
print(kombinasi(5,0))
print(kombinasi(1,1))
