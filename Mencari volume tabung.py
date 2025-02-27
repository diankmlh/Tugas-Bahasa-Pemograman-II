import math

jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))
tinggi_tabung = float(input("Masukkan tinggi tabung: "))
volume_tabung = math.pi * jari_jari_tabung ** 2 * tinggi_tabung
print(f"Volume tabung: {volume_tabung}")