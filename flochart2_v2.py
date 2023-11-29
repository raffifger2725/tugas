que = input("apakah anda ingin melakukan fibonacci? (y/n)")
ctr = 1
a = 1
b = 1
if que == "y":
    N = int(input("masukkan angka fibonacci: "))
    if ctr <=N :
        print(a)
    for i in range(N):
        c = a + b
        a = b
        b = c
        ctr = ctr + 1
        print(c)
else:
    print("thank you")

