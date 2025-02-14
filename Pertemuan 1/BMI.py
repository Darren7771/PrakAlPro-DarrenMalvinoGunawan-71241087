
# Kalkulator BMI 

str(input('Hai Selamat Datang Di KALKULATOR INDEKS MASSA TUBUH Silahkan Pencet Enter Untuk Melanjutkan...'))
Nama_Orang = str(input("Masukkan Nama: "))
berat = int(input("Masukkan Berat Badan (kg) : ") )
tinggi = float(input("Masukkan Tinggi Badan (m)(misal : tinggi 156 cm = 1.56 m : "))
total = berat / (tinggi*2)
BMI = "Indeks Massa Tubuh"
print(f"{BMI} : {total}")


if total <= 18.4:
    print(f'{Nama_Orang}, Maaf Sesuai BMI Kamu Kekurangan Berat Badan')
elif total <= 24.9:
    print(f'{Nama_Orang}, Selamat Kamu Normal')
elif total <= 39.9:
    print(f'{Nama_Orang}, Maaf Sesuai BMI Kamu Kelebihan Berat Badan')
else:
    print(f'{Nama_Orang},Mohon Maaf Sekali Menurut BMI Kamu Obesitas')
