status_list = ["Tetap", "Honor"]
golongan_list = ["A", "B", "C"]

print("\n===== RINCIAN GAJI PEGAWAI =====")
for status in status_list:
    for golongan in golongan_list:
        gaji = 1_000_000 if status == "Tetap" else 750_000
        bonus = {"A": 200_000, "B": 400_000, "C": 550_000} if status == "Tetap" else {"A": 150_000, "B": 275_000, "C": 480_000}
        
        gaji_total = gaji + bonus[golongan] 
        
        print("\n------------------------------")
        print(f"Status     : {status}")
        print(f"Golongan   : {golongan}")  
        print(f"Gaji Pokok : Rp{gaji:,}")
        print(f"Bonus      : Rp{bonus[golongan]:,}")  
        print(f"Gaji Total : Rp{gaji_total:,}")
print("\n===============================")
