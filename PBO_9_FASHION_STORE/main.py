import psycopg2
from utils import resetOS, header
import random
import string

class DatabaseFashionStore:
    def __init__(self, db_params):
        self.db_params = db_params
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.db_params)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
        if self.cursor:
            self.cursor.close()
        
    def display_etalase(self):
        self.cursor.execute("SELECT * FROM etalase")
        records = self.cursor.fetchall()
        print("|-------|-----------------|----------|----------|-------------|------|")
        print("|       |                 |    Daftar Etalase   |             |      |")
        print("|-------|-----------------|----------|----------|-------------|------|")
        print("| Kode  | Nama            | Ukuran   | Warna    | Harga       | Stok |")
        print("|-------|-----------------|----------|----------|-------------|------|")
        for record in records:
            print(f"| {record[0]:2} | {record[1]:<15} | {record[2]:<8} | {record[3]:<8} | {record[4]:<11} | {record[5]:<4} |")
        print("|-------|-----------------|----------|----------|-------------|------|")
    
    def chart(self,id,jumlah):
            random_angka = random.randint(10, 99)
            random_huruf = ''.join(random.choices(string.ascii_uppercase, k=3))
            kode = f"{random_angka}{random_huruf}"
            self.cursor.execute(f"SELECT * FROM etalase WHERE kode='{id}'")
            hasil = self.cursor.fetchone()
            total = hasil[4] * jumlah
            stok = hasil[5] - jumlah
            query = "INSERT INTO transaction(kode,nama,ukuran,warna,harga,jumlah,total) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            value = (kode,hasil[1],hasil[2],hasil[3],hasil[4],jumlah,total)
            self.cursor.execute(query,value)
            self.connection.commit()
            self.cursor.execute(f"UPDATE etalase SET stok={stok} WHERE kode='{id}'")
            self.connection.commit()
    
    def showChart(self):
        self.cursor.execute(f"SELECT * FROM transaction")
        records = self.cursor.fetchall()
        print("|-------|-----------------|----------|----------|-------------|--------|------------|")
        print("|       |                 |    Pembelian Anda   |             |        |            |")
        print("|-------|-----------------|----------|----------|-------------|--------|------------|")
        print("| Kode  | Nama            | Ukuran   | Warna    | Harga       | Jumlah | Total      |")
        print("|-------|-----------------|----------|----------|-------------|--------|------------|")
        for record in records:
            print(f"| {record[0]:<5} | {record[1]:<15} | {record[2]:<8} | {record[3]:<8} | {record[4]:<11} | {record[5]:<6} | {record[6]:<11}|")
        print("|-------|-----------------|----------|----------|-------------|--------|------------|")
        
    def deleteChart(self, kode):
        self.cursor.execute(f"DELETE FROM transaction WHERE kode='{kode}'")
        if self.cursor.rowcount > 0:
            self.connection.commit()
            return "DATA BERHASIL DIHAPUS"
        else:
            return "DATA TIDAK DITEMUKAN"
        
    def updateChart(self, kode, jumlah):
        self.cursor.execute(f"SELECT * FROM transaction WHERE kode='{kode}'")
        hasil = self.cursor.fetchone()
        total = hasil[4] * jumlah
        self.cursor.execute(f"UPDATE transaction SET jumlah={jumlah}, total={total} WHERE kode='{kode}'")
        self.connection.commit()
    
    def checkChart(self):
        self.cursor.execute(f"SELECT * FROM transaction")
        hasil = self.cursor.fetchall()
        if not hasil :
            return "keluar"

if __name__ == "__main__":
    # Mengganti nilai-nilai berikut sesuai dengan pengaturan database Anda
    db_params = {
        'dbname': '5220411245',
        'user': 'postgres',
        'password': 'thoriq2016',
        'host': 'localhost',
        'port': '5432'
    }

    # Membuat objek FashionStore
    fashion_store = DatabaseFashionStore(db_params)

    # Terhubung ke database
    fashion_store.connect()
    while True:
        resetOS()
        header()
        print('1. BELI BARANG')
        print('2. KELOLA KERANJANG')
        print('3. KELUAR')
        option = input('MASUKKAN NOMOR MENU: ')
        match option:    
            case '1':
                while True:
                    resetOS()
                    # Menampilkan etalase
                    fashion_store.display_etalase()
                    keranjang = input('PILIH KODE BARANG UNTUK MASUK KERANJANG: ')
                    jumlahBrg = int(input('TENTUKAN JUMLAH BARANG: '))
                    fashion_store.chart(keranjang,jumlahBrg)
                    option = input('APAKAH ADA BARANG LAGI (y/n): ')
                    if option.lower() != 'y': 
                        resetOS()
                        fashion_store.showChart()  
                        option = input('KELUAR? (PENCET APA AJA): ')
                        if option:
                            break
                    else:
                        continue

            case '2':
                resetOS()
                fashion_store.showChart()         
                
                print('1. UPDATE JUMLAH BARANG')
                print('2. HAPUS BARANG')
                print('3. KELUAR')

                option = input('MASUKKAN NOMOR MENU: ')
                if option == '1':
                    done = fashion_store.checkChart()   
                    if done == "keluar":
                        continue
                    else:
                        while True:
                            resetOS()
                            fashion_store.showChart()  
                            kode = input('PILIH KODE BARANG: ')
                            jumlah = int(input('MASUKKAN JUMLAH BARU: '))
                            fashion_store.updateChart(kode,jumlah)  
                            option = input('KELUAR? (y/n): ')
                            if option.lower() == 'y':
                                break
                            else:
                                continue
                elif option == '2':
                    done = fashion_store.checkChart()   
                    if done == "keluar":
                        continue
                    else:
                        while True:
                            resetOS()
                            fashion_store.showChart()  
                            kode = input('PILIH KODE BARANG YANG INGIN DIHAPUS : ')
                            hasil = fashion_store.deleteChart(kode)
                            if hasil == "DATA TIDAK DITEMUKAN":
                                print(hasil)
                                option = input('KELUAR? (y/n): ')
                                if option.lower() == 'y':
                                    break
                                else:
                                    continue
                            
                            option = input('INGIN HAPUS LAGI? (y/n)')
                            if option == 'y':
                                continue
                            else:
                                break
            case '3':
                # Menutup koneksi
                fashion_store.disconnect()
                exit()
