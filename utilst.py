# ==============================
# File        : utilst.py
# Modul       : Konversi Suhu
# ==============================

# Function Konversi Suhu
def konversi_suhu(nilai, dari, ke):
    
    # Validasi input satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return"Satuan tidak valid! Gunakan (C/F/K)."

    # Validasi input  nilai suhu tidak boleh negatif untuk kelvin
    if dari == "k" and nilai < 0:
        return"Nilai suhu dalam Kelvin tidak boleh negatif!"
        
    # Konversi suhu
    if dari == "c" and ke == "f":
        hasil = (nilai * 9/5) + 32
    elif dari == "c" and ke == "k":
        hasil = nilai + 273.15
    elif dari == "f" and ke == "c":
        hasil = (nilai - 32) * 5/9
    elif dari == "f" and ke == "k":
        hasil = (nilai - 32) * 5/9  + 273.15
    elif dari == "k" and ke == "c":
        hasil = nilai - 273.15
    elif dari == "k" and ke == "f":
        hasil = (nilai - 275.15) * 9/5 + 32
    # Jika satuan asal dan tujuan sama, maka akan return nilai dan menampilkan pesan error
    else:
        if dari == ke:
            return "Satuan asal dan tujuan tidak boleh sama!"
        
    # Validasi hasil konversi tidak boleh negatif untuk kelvin
    if ke == "k" and hasil < 0:
        return "Hasil konversi dalam Kelvin tidak boleh negatif!"
    
    return hasil

