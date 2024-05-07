Jumlah_Barang : []
Harga_Barang : []

while True :
    Jumlah_Barang : input("Masukkan Jumlah Barang")
    if Jumlah_Barang == "":
        break
Harga_Barang1 : float(input("Masukkan harga barang: "))
Harga_Barang2 : float(input("Masukkan harga barang: "))

Jumlah_Barang.append(Jumlah)
Harga_Barang1.append(Harga)
Harga_Barang2.append(Harga)

Total_Belanjaan = sum([jumlah * harga for jumlah, harga in zip(Jumlah_Barang, Harga_Barang)])
print("Total Belanjaan: Rp. ", total_harga)