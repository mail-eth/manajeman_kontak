# manajemen kontak
def MembukaKontak(path='kontak.txt'):
    try:
        with open(path, 'r') as file:
            kontak = file.readlines()
            return kontak
    except FileNotFoundError:
        return []
def MenyimpanKontak(path='kontak.txt', isi=[]):
    with open(path, 'w') as file:
        file.writelines(isi)
class Kontak:
    def __init__(self):
        self.kontak = MembukaKontak()
    def lihat_kontak(self):
        if self.kontak:
            for num,item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + ''.join(item))
                    
        else:
                print("kontak kosong")
                return 1
    def menambah_kontak(self):
        nama = input("Masukkan nama kontak: ")
        hp =input ("Masukkan Nomor HP kontak: ")
        email =input ("Masukkan Email kontak: ")
        kontak_baru = f"{nama} ( HP {hp}, {email}) \n"
        self.kontak.append(kontak_baru)
        print('kontak berhasil di tambahkan')

    def menghapus_kontak(self):
        if self.lihat_kontak() == 1:
            return
        else:
            try:
                i = int(input("Masukkan nomor yang mau di hapus: "))
                del self.kontak[i-1]
            except:
                print("Input yang anda masukkan salah")


kontak_rumah = Kontak()
kontak_sekolah = Kontak()

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
        MenyimpanKontak(isi=kontak_rumah.kontak)
        break

    else:
        print("Terima kasih telah menggunakan program ini")
        break

            