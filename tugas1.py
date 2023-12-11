import os

DATA_FILE = "data_mahasiswa_umm.txt"

def tambah_data():
    print("===== Tambah Data Mahasiswa =====")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    matkul = input("Masukkan Mata Kuliah: ")
    semester = input("Masukkan Semester: ")

    with open(DATA_FILE, "a") as file: #memulai data baru
        file.write(f"{nama},{nim},{matkul},{semester}\n")

    print("Data mahasiswa berhasil ditambahkan.")

def tampilkan_data():
    print("===== Tampilkan Data Mahasiswa =====")
    with open(DATA_FILE, "r") as file:
        lines = file.readlines()
        if not lines:
            print("Belum ada data mahasiswa.")
        else:
            for i, line in enumerate(lines, 1):
                nama, nim, matkul, semester = line.strip().split(',')
                print(f"Data ke-{i}:")
                print(f"Nama: {nama}")
                print(f"NIM: {nim}")
                print(f"Mata Kuliah: {matkul}")
                print(f"Semester: {semester}")
                print()

def update_data():
    print("===== Update Data Mahasiswa =====")
    nim_update = input("Masukkan NIM dari data yang ingin diubah: ")

    with open(DATA_FILE, "r") as file:
        lines = file.readlines()

    updated = False
    with open(DATA_FILE, "w") as file:
        for line in lines:
            nama, nim, matkul, semester = line.strip().split(',')
            if nim == nim_update:
                nama_baru = input("Masukkan Nama Baru: ")
                nim_baru = input("Masukkan NIM Baru: ")
                matkul_baru = input("Masukkan Mata Kuliah Baru: ")
                semester_baru = input("Masukkan Semester Baru: ")
                file.write(f"{nama_baru},{nim_baru},{matkul_baru},{semester_baru}\n")
                updated = True
            else:
                file.write(line)
    if updated:
        print("Data berhasil diupdate.")
    else:
        print("NIM tidak ditemukan. Data tidak diupdate.")

def delete_data():
    print("===== Delete Data Mahasiswa =====")
    nim_delete = input("Masukkan NIM data yang ingin dihapus: ")

    with open(DATA_FILE, "r") as file:
        lines = file.readlines()

    deleted = False
    with open(DATA_FILE, "w") as file:
        for line in lines:
            nama, nim, matkul, semester = line.strip().split(',')
            if nim == nim_delete:
                deleted = True
            else:
                file.write(line)

    if deleted:
        print("Data berhasil dihapus.")
    else:
        print("NIM tidak ditemukan. Data tidak dihapus.")

def search_data():
    print("===== Search Data Mahasiswa =====")
    nim_search = input("Masukkan NIM dari data yang ingin dicari: ")

    with open(DATA_FILE, "r") as file:
        for line in file:
            nama, nim, matkul, semester = line.strip().split(',')
            if nim == nim_search:
                print(f"Nama: {nama}")
                print(f"NIM: {nim}")
                print(f"Mata Kuliah: {matkul}")
                print(f"Semester: {semester}")
                print()
                break
        else:
            print("Data tidak ditemukan.")

def main():
    while True:
        print("===== APLIKASI KELOLA DATA MAHASISWA UMM =====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Search Data")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            update_data()
        elif pilihan == '4':
            delete_data()
        elif pilihan == '5':
            search_data()
        elif pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()
