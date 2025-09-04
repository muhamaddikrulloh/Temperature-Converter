from utilst import (
    konversi_suhu
)

while True:
    try:
        print("=== KONVERSI SUHU ===")
        
        # Input nilai dan satuan suhu dari user
        nilai = float(input("Masukan nilai suhu: "))
        dari = input("Dari satuan (C/F/K): ").lower()
        ke = input("Ke satuan (C/F/K): ").lower()

        # Output hasil konversi
        hasil_funct = konversi_suhu(nilai, dari, ke)
        # jika hasil fungsi adalah string karena nilai awal & tujuan sama, maka akan menampilkan pesan error
        if isinstance(hasil_funct, str):
            print(f"Error: {hasil_funct}")
        else:
            print(f"Hasil: {nilai:.0f}°{dari.upper()} = {hasil_funct:.1f}°{ke.upper()}")
          
    # Handing invalid input        
    except ValueError:
        print("Input tidak valid! Masukan angka untuk nilai suhu.")
        continue
    
    # Tanya user untuk konversi lagi    
    lagi = input("Ingin melakukan konversi lagi? (y/n)").lower()
    if lagi != "y":
        print("=== Program selesai. ===")
        break
        
