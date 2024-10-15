# manajemen kontak
# 1. lihat kontak

import dokumen
class Kontak:
    def __init__(self):
        self.kontak = dokumen.MembukaKontak()

    def lihat_kontak(self):
        if self.kontak:
            print("Daftar Kontak:")
            for num,item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + ''.join(item))

                    
        else:
                print("kontak kosong")
                return 1
    def menambah_kontak(self):
        print("Tambah Kontak")
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

