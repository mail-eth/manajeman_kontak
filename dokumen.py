# membuka kontak dan menyimpan kontak
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