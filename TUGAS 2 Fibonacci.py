data = int(input(" Masukkan Jumlah Deret Fibonacci: "))
n1 = 0
n2 = 1
hasil = []
for i in range(data):
    hasil.append(n1)
    total = n1 + n2
    n1 = n2
    n2 = total

print(hasil)    