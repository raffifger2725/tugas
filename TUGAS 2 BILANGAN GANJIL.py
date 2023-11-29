bilanganganjil = []
n = 1 

while len(bilanganganjil) < 8:
    bilanganganjil.append(n)
    n += 2

output = ', '.join(map(str, bilanganganjil))

print("Hasil output:", output)