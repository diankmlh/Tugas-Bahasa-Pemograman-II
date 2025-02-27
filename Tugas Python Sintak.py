import math

print("1. Mencari Luas Segitiga")
alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
luas_segitiga = 0.5 * alas * tinggi
print(f"Luas segitiga: {luas_segitiga}")
print()

print("2. Mencari Luas Persegi Panjang")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
luas_persegi_panjang = panjang * lebar
print(f"Luas persegi panjang: {luas_persegi_panjang}")
print()

print("3. Mencari Luas Luas")
jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas_lingkaran = math.pi * jari_jari ** 2
print(f"Luas lingkaran: {luas_lingkaran}")
print()

print("4. Mencari Volume Tabung")
jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))
tinggi_tabung = float(input("Masukkan tinggi tabung: "))
volume_tabung = math.pi * jari_jari_tabung ** 2 * tinggi_tabung
print(f"Volume tabung: {volume_tabung}")
print()
