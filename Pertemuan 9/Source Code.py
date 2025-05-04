file = open('contohFile.txt') #mode biasa jadi read
file2 = open('contohFile.txt','w') # ini mode write yang ada w nya
print(file,file2)

with open('contohFile.txt') as file:


file = open('contohlain.txt')
print(file)

fileHitung = open("contohFile.txt", "r")
for line in fileHitung:
    nama,Nilai= line.strip().split(": ")
    if int(Nilai) >= 75:
        print(nama, Nilai)

cariEmail = open("file email.txt")
angka = 1
for line in cariEmail:
    pemisah = line.strip().split()
    for email in pemisah:
        if '@' in email and "." in email:
            print(f"{angka}.email : {email}")
            angka += 1
            # outputnya
            # 1.dodon@gmail.com
            # 2.tttoekboks@co.id
            # 3.koari@yahoo.com
            # 4.poerwo88@student.co.id 
    
contoh = open('contohFIle.txt','w')
kataBaru = "hai hai hai haiahi haihiahiahihaiah"
contoh.write(kataBaru)

contoh = open('contohFIle.txt','a')
kataBaru = "michael : 90"
contoh.append(kataBaru)
