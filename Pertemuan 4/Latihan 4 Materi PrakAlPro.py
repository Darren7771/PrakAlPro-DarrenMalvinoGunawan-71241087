# NilaiAkhir = 90 
# if NilaiAkhir > 80 :
#     print("Lulus")
# else: 
#     print("Tidak Lulus")

# Tinggi = int(input("Masukkan Tinggi Badan anda dalam (CM) : "))

# if Tinggi > 170:
#     print("Tinggi Ideal")
# elif Tinggi > 160:
#     print ("Tinggi Rata-Rata Orang Indonesia")
# elif Tinggi > 140:
#     print("Pendek banget kau")
# else: 
#     print("CEPER")

try:
    beratBadan = input("Masukkan Berat Anda (Kg) : ")
    tinggiBadan = input("Masukkan Tinggi Anda (m)(188 cm = 1.88 m ) : ")
    BMI = beratBadan / (tinggiBadan**2)
    
    BMI = float (beratBadan and tinggiBadan)

    if BMI < 18.5:
        print("Kekurangan Berat Badan")
    elif BMI >= 18.5 and BMI<25:
        print("Normal")
    elif BMI >= 25 and BMI < 30:
        print("Kelebihan Berat Badan")
    else:
        print("Obes")
except Exception as e:
    print("Jangan Menggunakan Huruf / kata2 , gunakan angka.")
    print(e)
