import kontak
import dokumen

def main():
    # TODO: Membuat class kontak
    kontak_rumah = kontak.Kontak()
    kontak_sekolah = kontak.Kontak()

    while True:
        print("\nManajemen kontak")
        print("1. lihat kontak")
        print("2. Menambahkan kontak")
        print("3. Menghapus kontak")
        print("4. Keluar dari kontak")

        pilihan = input("Masukkan pilihan anda (1,2,3 atau 4) : ")

        if pilihan == '1':
            kontak_rumah.lihat_kontak()

        elif pilihan == '2':
            kontak_rumah.menambah_kontak()

            
        elif pilihan == '3':
            # menghapus kontak
            kontak_rumah.menghapus_kontak()
        elif pilihan == '4':
            # keluar dari program
            dokumen.MenyimpanKontak(isi=kontak_rumah.kontak)
            break

        else:
            print("Terima kasih telah menggunakan program ini")
            break

if __name__ == "__main__":
    main()
                