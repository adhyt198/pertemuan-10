# Program Daftar Nilai Mahasiswa Menggunakan Dictionary

mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    mahasiswa[nama] = {
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": nilai_akhir
    }
    print("Data berhasil ditambahkan!\n")

def ubah_data():
    nama = input("Masukkan nama yang akan diubah: ")
    if nama in mahasiswa:
        tugas = float(input("Nilai Tugas baru: "))
        uts = float(input("Nilai UTS baru: "))
        uas = float(input("Nilai UAS baru: "))
        
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        mahasiswa[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": nilai_akhir
        }
        print("Data berhasil diubah!\n")
    else:
        print("Nama tidak ditemukan!\n")

def hapus_data():
    nama = input("Masukkan nama yang akan dihapus: ")
    if nama in mahasiswa:
        del mahasiswa[nama]
        print("Data berhasil dihapus!\n")
    else:
        print("Nama tidak ditemukan!\n")

def tampilkan_data():
    if not mahasiswa:
        print("Belum ada data.\n")
        return
    print("===== Daftar Nilai Mahasiswa =====")
    for nama, nilai in mahasiswa.items():
        print(f"Nama: {nama}")
        print(f"  Tugas : {nilai['tugas']}")
        print(f"  UTS   : {nilai['uts']}")
        print(f"  UAS   : {nilai['uas']}")
        print(f"  Akhir : {nilai['akhir']:.2f}")
        print("----------------------------------")
    print()

def cari_data():
    nama = input("Masukkan nama yang dicari: ")
    if nama in mahasiswa:
        nilai = mahasiswa[nama]
        print(f"Nama: {nama}")
        print(f"  Tugas : {nilai['tugas']}")
        print(f"  UTS   : {nilai['uts']}")
        print(f"  UAS   : {nilai['uas']}")
        print(f"  Akhir : {nilai['akhir']:.2f}\n")
    else:
        print("Data tidak ditemukan!\n")

# Menu Utama
while True:
    print("=== MENU ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        ubah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        tampilkan_data()
    elif pilihan == "5":
        cari_data()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!\n")
