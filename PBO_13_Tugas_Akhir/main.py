class Fashion():
    def __init__(self, jumlah, merek, ukuran, warna, harga):
        self.__jumlah = jumlah
        self.merek = merek
        self.ukuran = ukuran
        self.warna = warna
        self.__harga = harga
    
    def tampil(self):
        print(f"Jumlah Barang\t: {self.__jumlah}")
        print(f"Merek\t\t: {self.merek}")
        print(f"Ukuran\t\t: {self.ukuran}")
        print(f"Warna\t\t: {self.warna}")
        print(f"Harga\t\t: {self.__harga}")

class Baju(Fashion):
    def __init__(self, jumlah, merek, ukuran, warna, harga, jenis_baju):
        super().__init__(jumlah, merek, ukuran, warna, harga)
        self.jenis_baju = jenis_baju
    
    def tampil(self):
        super().tampil()
        print(f"Jenis Baju\t: {self.jenis_baju}")

class Jaket(Baju):
    def __init__(self, jumlah, merek, ukuran, warna, harga, jenis_baju, model):
        super().__init__(jumlah, merek, ukuran, warna, harga, jenis_baju)
        self.model = model
    def tampil(self):
        super().tampil()
        print(f"Model Jaket\t: {self.model}")

class Celana(Fashion):
    def __init__(self, jumlah, merek, ukuran, warna, harga, jenis_celana):
        super().__init__(jumlah, merek, ukuran, warna, harga)
        self.jenis_celana = jenis_celana

    def tampil(self):
        super().tampil()
        print(f"Jenis Celana\t: {self.jenis_celana}")

class Order():
    def __init__(self, items):
        self.__items = items
    
    def hitung_harga(self):
        total = 0
        for item in self.__items:
            total += item._Fashion__harga * item._Fashion__jumlah
        return total
    
    def hitung_diskon(self, total):
        if total >= 500000:
            diskon = ((total * 10)/100)  
            afterDiskon = total - diskon
            return afterDiskon
        elif total >= 300000:
            diskon = ((total * 5)/100) 
            afterDiskon = total - diskon
            return afterDiskon 
        else:
            return total

    def tampilan_order(self):
        print("\nOrder Details:")
        for item in self.__items:
            item.tampil()
            print("------------------------------")
        total = self.hitung_harga()
        discounted_total = self.hitung_diskon(total)

        print(f"\nTotal Pembayaran sebelum Diskon: {total}")
        
        if discounted_total < total:
            print(f"Diskon diterapkan! Total Pembayaran setelah Diskon: {int(discounted_total)}")
        else:
            print("Tidak ada diskon diterapkan.")
        
        print("\nTerima kasih atas pembelian Anda!\n")

if __name__ == '__main__':
    objekBaju = Baju(2, 'Kupakai', 'L', 'Hitam', 50000, 'Kaos Polos')
    objekJaket = Jaket(2, 'The King Slumdunk', 'XL', 'Hitam', 200000, 'Jaket', 'Varsity')
    objekCelana = Celana(2, 'Uniqlo', 'L', 'Hitam', 120000, 'Chino')

    order_items = [objekBaju, objekJaket, objekCelana]

    objekOrder = Order(order_items)
    objekOrder.tampilan_order()