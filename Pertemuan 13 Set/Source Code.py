cobalist = {'1','2','3','4','5','3'}                    #kalo ada yang sama akan dijadikan satu
coba = {1,2,3,4,5}
orang = set(["putra","bendot","coki"])
setKosong = set()
print(cobalist)
print(coba)
print(orang)
print(setKosong)

makanan = {"bakso","ayam goreng", "soto", "nasi goreng"}
print(f"Jumlahnya : {len(makanan)} ") 
for i in makanan:
    print(i)

bilangan = {1,2,4,5,6,7}
bilangan.remove(7)          
print(bilangan) 

bilangan2 = {9,4,10,1,5,3,7}
bilangan2 = {"a","2","ss"}
bilangan2.pop() 
print(bilangan2)

bilangan3 = {1,8,3,9}
bilangan3.add(5)
print(bilangan3)

angka = {1,35,33,2}
angka.add(5)
print(sorted(angka))

nilai = {100,99,77,87,98}
nilai.add(3)
nilai.pop()
nilai.remove(77)
print(sorted(nilai))


kelasA = {"darren", "doni","bubu"}
kelasB = {"koko", "cici","babi", "bubu"}

hasil = kelasA | kelasB 
# hasil = kelasA.union(kelasB) 
hasil2 = kelasA & kelasB
# hasil2 = kelasA.intersection(kelasB)
hasil3 = kelasA - kelasB
hasil3 = kelasA.difference(kelasB)
hasil4 = kelasA ^ kelasB
# hasil4 = kelasA.symmetric_difference(kelasB)

print("1.",hasil)
print("2.",hasil2)
print("3.",hasil3)
print("4.",hasil4)

a = {"doni","peter","vano"}
b = {"peter", "boni", "gareng"}
c = {"radit","adit","gareng"}

sama = a & b 
sama2 = c & b 
gabungan = sama | sama2
total = gabungan ^ a 

print(f'(a & b ) : ',sama)
print(f'(b & c ) : ',sama2)
print(f'(a & b ) | (b & c ) : ',gabungan)
print(f'((a & b ) | (b & c )) ^ a : ',total)



def perbandingan_hobi():
    nama1 = input("Nama orang pertama: ")
    hobi1 = set(input(f"Masukkan hobi {nama1} (pisahkan dengan koma): ").strip().split(','))
    nama2 = input("Nama orang kedua: ")
    hobi2 = set(input(f"Masukkan hobi {nama2} (pisahkan dengan koma): ").strip().split(','))
    hobi1 = {h.strip() for h in hobi1}
    hobi2 = {h.strip() for h in hobi2}
    sama = hobi1.intersection(hobi2)
    gabungan = hobi1.union(hobi2)
    unik1 = hobi1.difference(hobi2)
    print(f"\nHobi yang sama antara {nama1} dan {nama2}: {sama}")
    print("Gabungan semua hobi:", gabungan)
    print(f"Hobi yang hanya dimiliki {nama1}:", unik1)
perbandingan_hobi()
