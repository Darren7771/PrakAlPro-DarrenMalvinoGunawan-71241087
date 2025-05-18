# """Jawaban No 1"""
# def MenghitungDict(Dictionary):
#     print("key\tvalue\titems")
#     for key,value in Dictionary.items():
#         print(f"{key}\t{value}\t{key}")
# MenghitungDict({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})

"""Jawaban No 2"""
def gabungDictionary(Lista,Listb):
    hasil = {}
    for i in Lista:
        indeks = Lista.index(i)
        hasil[i] = Listb[indeks]
    print(hasil)

gabungDictionary(['red', 'green', 'blue'], 
    ['#FF0000','#008000', '#0000FF'])


    


