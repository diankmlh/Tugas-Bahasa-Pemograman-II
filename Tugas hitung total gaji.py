# 1. Buat inputan
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Tetap/Honor): ")  # 5. Status merupakan inputan string
golongan = input("Masukkan Golongan (A/B/C): ") # 5. Golongan merupakan inputan string

# 2. Jika status Pegawai Tetap
if status.lower() == "tetap":
    gaji = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
    else:
        bonus = 0  # Jika golongan tidak valid

# 3. Jika status Pegawai Honor
elif status.lower() == "honor":
    gaji = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000
    else:
        bonus = 0  # Jika golongan tidak valid

# Jika status tidak valid
else:
    gaji = 0
    bonus = 0

# 4. Print Gaji, Bonus, dan Gaji Total
print("\n===== Detail Gaji =====")
print(f"Nama       : {nama}")
print(f"NIK        : {nik}")
print(f"Status     : {status}")  
print(f"Golongan   : {golongan}")  
print(f"Gaji Pokok : Rp{gaji:,}")
print(f"Bonus      : Rp{bonus:,}")  
print(f"Gaji Total : Rp{gaji_total:,}")  