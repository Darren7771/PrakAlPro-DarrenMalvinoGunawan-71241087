def kombinasi(n,r):
    if n == r or r == 0:
        return 1 
    else:
        return kombinasi(n-1,r) + kombinasi (n-1,r-1)
print(kombinasi(5,2))
print(kombinasi(5,0))
print(kombinasi(1,1))