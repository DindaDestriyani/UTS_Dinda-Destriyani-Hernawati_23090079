tahun : int(input("Masukkan Tahun : "))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print(f"{tahun} adalah Tahun Kabisat")
        else:
            print(f"{tahun} bukan Tahun Kabisat")
    else:
        print(f"{tahun} adalah Tahun Kabisat")
else:
    print(f"{tahun} bukan Tahun Kabisat")
