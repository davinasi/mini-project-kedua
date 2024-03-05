# davina putri izzati gautama
# 2309116054

from prettytable import PrettyTable

class Node:
    def __init__(self, id_produk, nama, kategori, harga, jumlah):
        self.id_produk = id_produk
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.jumlah = jumlah
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_node_di_awal(self, id_produk, nama, kategori, harga, jumlah):
        new_node = Node(id_produk, nama, kategori, harga, jumlah)
        new_node.next = self.head
        self.head = new_node

    def tambah_node_di_akhir(self, id_produk, nama, kategori, harga, jumlah):
        new_node = Node(id_produk, nama, kategori, harga, jumlah)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def tambah_node_di_antara(self, prev_id_produk, id_produk, nama, kategori, harga, jumlah):
        new_node = Node(id_produk, nama, kategori, harga, jumlah)
        current = self.head
        while current and current.id_produk != prev_id_produk:
            current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node

    def lihat_produk(self):
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Kategori", "Harga", "Jumlah"]
        current = self.head
        while current:
            tabel.add_row([current.id_produk, current.nama, current.kategori, current.harga, current.jumlah])
            current = current.next
        print(tabel)

    def hapus_node_di_awal(self):
        if not self.head:
            print("Tidak ada produk untuk dihapus.")
            return
        self.head = self.head.next

    def hapus_node_di_akhir(self):
        if not self.head:
            print("Tidak ada produk untuk dihapus.")
            return
        if not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def hapus_node_di_antara(self, id_produk):
        if not self.head:
            print("Tidak ada produk untuk dihapus.")
            return
        if self.head.id_produk == id_produk:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.id_produk != id_produk:
            current = current.next
        if current.next:
            current.next = current.next.next

class TokoLego:
    def __init__(self):
        self.produk_list = LinkedList()

    def tambah_produk(self, id_produk, nama, kategori, harga, jumlah):
        self.produk_list.tambah_node_di_akhir(id_produk, nama, kategori, harga, jumlah)

    def lihat_produk(self):
        self.produk_list.lihat_produk()

    def hapus_produk(self, id_produk):
        self.produk_list.hapus_node_di_antara(id_produk)

    def menu_crud(self):
        # product dumpies
        self.tambah_produk(60248, 'police station', 'LEGO City', 1.945, 100)
        self.tambah_produk(70668, 'LEGACY Jays Storm Fighter', 'LEGO Ninjago', 1.850, 50)
        self.tambah_produk(43206, 'Cinderella Castle', 'LEGO Disney princess', 1.599, 30)
        self.tambah_produk(43241, 'Rapunzels Tower', 'LEGO Disney princess', 1.599, 10)
        self.tambah_produk(76401, 'Hogwarts Courtyard', 'LEGO Harry Potter', 971 , 30)

        while True:
            print("===============================================")
            print(" Selamat datang di Sistem Manajemen Toko LEGO: ")
            print("===============================================")
            print("1. Tambah Produk")
            print("2. Lihat Produk")
            print("3. Hapus Produk")
            print("4. Keluar")

            pilihan = input("Pilih Menu (1-4): ")

            if pilihan == '1':
                id_produk = int(input("Masukkan ID Produk: "))
                nama = input("Masukkan Nama Produk: ")
                kategori = input("Masukkan Kategori Produk: ")
                harga = float(input("Masukkan Harga Produk: "))
                jumlah = int(input("Masukkan Jumlah Produk: "))
                self.tambah_produk(id_produk, nama, kategori, harga, jumlah)

            elif pilihan == '2':
                self.lihat_produk()

            elif pilihan == '3':
                id_produk = int(input("Masukkan ID Produk yang ingin dihapus: "))
                self.hapus_produk(id_produk)

            elif pilihan == '4':
                print("Terima kasih! Keluar dari program.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    toko_lego = TokoLego()
    toko_lego.menu_crud()
