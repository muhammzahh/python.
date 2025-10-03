angka = 10
nama = "Python"
daftar_buah = ["apel", "pisang", "jeruk"]


print(type(angka))
print(type(nama))
print(type(daftar_buah))
belanja = ["beras", "minyak", "telur"]


belanja.append("gula")
belanja.append("kopi")


for item in belanja:
    print(item)


harga = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}


total = sum(harga.values())

print("Total harga semua belanjaan adalah:", total)

import math

def hitung_lingkaran(jari_jari):
    luas = math.pi * jari_jari**2
    keliling = 2 * math.pi * jari_jari
    return luas, keliling


jari_jari = 7
luas, keliling = hitung_lingkaran(jari_jari)
print(f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")


usia = int(input("Masukkan usia Anda: "))


if usia >= 0 and usia <= 13:
    print("Anak")
elif usia >= 14 and usia <= 24:
    print("Remaja")
elif usia >= 25 and usia <= 49:
    print("Dewasa")
elif usia >= 50:
    print("Lansia")
else:
    print("Usia tidak valid")