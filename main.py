def tampilkan_menu():
    print("===============================")
    print("  SELAMAT DATANG DI SI-HADIR  ")
    print("===============================")
    print("1. Kelola Anggota")
    print("2. Kelola Divisi")
    print("3. Kelola Kegiatan")
    print("4. Proses Absensi")
    print("5. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Plih Menu (1-5): ")

        if pilihan == "1":
            print("\n[Menu Anggota belum diimpor]\n")
        elif pilihan == "2":
            print("\n[Menu Divisi belum diimpor]\n")
        elif pilihan == "3":
            print("\n[Menu Kegiatan belum diimpor]\n")
        elif pilihan == "4":
            print("\n[Menu Absensi belum diimpor]"\n)
        elif pilihan == "5":
            print("\nTerima kasih telah menggunkan SI-HADIR!")
            break
        else:
            print("\nPilihan tidak valid. Solahkan coba lagi.\n")

if __name__ == "__main__":
    main()
    
