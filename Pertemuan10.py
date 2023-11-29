daftar_angka=(199,399,699,999)
print("Daftar Angka")
for angka in daftar_angka:
    print(angka)
nomor = int(input("Masukkan 3 Digit Angka: "))
if nomor in daftar_angka:
    posisi = daftar_angka.index(nomor)
    print(f"Nomor {nomor} ditemukan pada posisi {posisi + 1}dalam daftar")
else:
    print("nomor tidak terdaftar")
    