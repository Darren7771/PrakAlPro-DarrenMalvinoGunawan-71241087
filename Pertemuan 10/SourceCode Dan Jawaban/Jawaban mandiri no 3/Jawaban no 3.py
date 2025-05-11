def unik():
    print("=======Program Pencari Kata Unik========")
    with open("Latihan Py\Jawaban mandiri no 3\\berita.txt","r") as fileBerita:
        teks = fileBerita.read()

    kata = teks.split()
    
    kataUnik = []
    kataHanya1 = []

    for i in set(kata):
        if kata.count(i) > 1:
            kataUnik.append(i)
        else:
            kataHanya1.append(i)
    if kataUnik: 
        print("Kata Unik / Yang muncul lebih dari 1 kali : ")
        print(kataUnik)
    if kataHanya1:
        print("\nKata yang muncul hanya 1 kali :")
        print(kataHanya1)
    print("\n==============Program Selesai==============")

unik()