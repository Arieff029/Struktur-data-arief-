
harga_ayam = [
    {"jenis": "krispi", "ukuran": {"kecil": 10000, "sedang": 15000, "besar": 20000}},
    {"jenis": "original", "ukuran": {"kecil": 9000, "sedang": 14000, "besar": 19000}},
    {"jenis": "pedas", "ukuran": {"kecil": 11000, "sedang": 16000, "besar": 21000}},
]


pesanan = []  

def tampilkan_jenis_ayam():
    """Menampilkan semua jenis ayam dan harga per ukuran."""
    print("\nJenis Ayam dan Harga:")
    for data in harga_ayam:
        print(f"\nJenis Ayam: {data['jenis']}")
        for ukuran, harga in data["ukuran"].items():
            print(f"  - Ukuran {ukuran}: Rp{harga}")


def cari_jenis_ayam():
    """Mencari ayam berdasarkan nama jenis."""
    nama_jenis = input("Masukkan nama jenis ayam yang dicari: ")
    nama_jenis = nama_jenis.lower()
    for data in harga_ayam:
        if data["jenis"] == nama_jenis:
            print(f"\nJenis Ayam: {nama_jenis}")
            for ukuran, harga in data["ukuran"].items():
                print(f"  - Ukuran {ukuran}: Rp{harga}")
            return
    print(f"Jenis ayam '{nama_jenis}' tidak ditemukan.")


def urutkan_harga_ayam():
    """Mengurutkan harga ayam berdasarkan harga menggunakan Bubble Sort."""
    print("\nHarga Ayam Diurutkan (Termurah ke Termahal):")
    ayam_urut = []
    for data in harga_ayam:
        for ukuran, harga in data["ukuran"].items():
            ayam_urut.append({"jenis": data["jenis"], "ukuran": ukuran, "harga": harga})


    n = len(ayam_urut)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ayam_urut[j]["harga"] > ayam_urut[j + 1]["harga"]:
                ayam_urut[j], ayam_urut[j + 1] = ayam_urut[j + 1], ayam_urut[j]

    for item in ayam_urut:
        print(f"{item['jenis']} - Ukuran {item['ukuran']}: Rp{item['harga']}")


def pesan_ayam():
    """Membuat pesanan ayam"""
    global pesanan  
    print("\nPilih jenis ayam:")
    for index, data in enumerate(harga_ayam, start=1):
        print(f"{index}. {data['jenis']}")

    jenis_pilihan = int(input("Masukkan nomor pilihan: "))
    jenis = harga_ayam[jenis_pilihan - 1]["jenis"]

    print("\nPilih ukuran ayam:")
    ukuran_keys = list(harga_ayam[jenis_pilihan - 1]["ukuran"].keys())
    for index, ukuran in enumerate(ukuran_keys, start=1):
        print(f"{index}. {ukuran}")

    ukuran_pilihan = int(input("Masukkan nomor pilihan: "))
    ukuran = ukuran_keys[ukuran_pilihan - 1]

    jumlah = int(input("Masukkan jumlah pesanan: "))
    harga_total = harga_ayam[jenis_pilihan - 1]["ukuran"][ukuran] * jumlah

    baru = [{"jenis": jenis, "ukuran": ukuran, "jumlah": jumlah, "harga_total": harga_total}]
    pesanan = pesanan + baru

    print(f"\nPesanan berhasil ditambahkan: {jumlah} ayam {jenis} ukuran {ukuran} dengan total harga Rp{harga_total}")


def tampilkan_pesanan():
    """Menampilkan semua pesanan dalam antrian."""
    if not pesanan:
        print("\nBelum ada pesanan.")
        return

    print("\nDaftar Pesanan:")
    for i, order in enumerate(pesanan, start=1):
        print(f"{i}. {order['jumlah']} ayam {order['jenis']} ukuran {order['ukuran']} - Total: Rp{order['harga_total']}")


while True:
    print("\nMenu:")
    print("1. Tampilkan Jenis Ayam dan Harga")
    print("2. Cari Ayam")
    print("3. Urutkan Harga Ayam")
    print("4. Buat Pesanan")
    print("5. Tampilkan Hasil Pesanan")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_jenis_ayam()
    elif pilihan == "2":
        cari_jenis_ayam()
    elif pilihan == '3':
        urutkan_harga_ayam()
    elif pilihan == '4':
        pesan_ayam()
    elif pilihan == '5':
        tampilkan_pesanan()
    elif pilihan == '6':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
