print("=== Sistem Reservasi Hotel ===")
reservasi = {}

while True:
    print("Menu:")
    print("1. Tambah Reservasi")
    print("2. Update Reservasi")
    print("3. Hapus Reservasi")
    print("4. Lihat Semua Reservasi")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama tamu: ")
        if nama in reservasi:
            print("Nama sudah terdaftar, gunakan nama lain yang belum terdaftar")
        else:
            print("Jenis kamar yang tersedia:")
            print("1. Kamar Standard - Rp 500.000 per malam")
            print("2. Kamar Deluxe - Rp 800.000 per malam")
            print("3. Kamar Suite - Rp 1.200.000 per malam")
            kamar_pilihan = input("Masukkan nomor jenis kamar (1/2/3): ")
            if kamar_pilihan == "1":
                jenis_kamar = "Standard"
                harga = 500000
            elif kamar_pilihan == "2":
                jenis_kamar = "Deluxe"
                harga = 800000
            elif kamar_pilihan == "3":
                jenis_kamar = "Suite"
                harga = 1200000
            else:
                print("Pilihan kamar tidak tersedia.")
                continue

            lama = input("Masukkan lama menginap (malam): ")
            if lama.isdigit():
                lama = int(lama)
                if lama <= 0:
                    print("Lama menginap harus lebih dari 0.")
                    continue
            else:
                print("Input lama menginap tidak valid.")
                continue

            total = harga * lama
            reservasi[nama] = {"kamar": jenis_kamar, "lama": lama, "total": total}
            print(f"Reservasi untuk {nama} berhasil ditambahkan.")

    elif pilihan == "2":
        nama = input("Masukkan nama tamu yang ingin diupdate: ")
        if nama in reservasi:
            print(f"Data saat ini: {reservasi[nama]}")
            print("Jenis kamar yang tersedia:")
            print("1. Kamar Standard - Rp 500.000 per malam")
            print("2. Kamar Deluxe - Rp 800.000 per malam")
            print("3. Kamar Suite - Rp 1.200.000 per malam")
            kamar_pilihan = input("Masukkan nomor jenis kamar (1/2/3): ")
            if kamar_pilihan == "1":
                jenis_kamar = "Standard"
                harga = 500000
            elif kamar_pilihan == "2":
                jenis_kamar = "Deluxe"
                harga = 800000
            elif kamar_pilihan == "3":
                jenis_kamar = "Suite"
                harga = 1200000
            else:
                print("Pilihan kamar tidak tersedia.")
                continue

            lama = input("Masukkan lama menginap (malam): ")
            if lama.isdigit():
                lama = int(lama)
                if lama <= 0:
                    print("Lama menginap harus lebih dari 0.")
                    continue
            else:
                print("Input lama menginap tidak valid.")
                continue

            total = harga * lama
            reservasi[nama] = {"kamar": jenis_kamar, "lama": lama, "total": total}
            print(f"Reservasi untuk {nama} berhasil diupdate.")
        else:
            print("Reservasi tidak ditemukan.")

    elif pilihan == "3":
        nama = input("Masukkan nama tamu yang ingin dihapus reservasinya: ")
        if nama in reservasi:
            del reservasi[nama]
            print(f"Reservasi untuk {nama} berhasil dihapus.")
        else:
            print("Reservasi tidak ditemukan.")

    elif pilihan == "4":
        if len(reservasi) == 0:
            print("Belum ada reservasi.")
        else:
            print("\nDaftar Reservasi:")
            for nama, data in reservasi.items():
                print(f"- {nama}: Kamar {data['kamar']}, {data['lama']} malam, Total Rp {data['total']:,}")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan sistem reservasi.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
''
