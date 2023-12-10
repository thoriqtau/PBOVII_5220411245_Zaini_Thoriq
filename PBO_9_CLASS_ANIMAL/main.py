class Animal():
  def __init__(self, nama, sifat, ukuran, jumlah_kaki):
    self.__nama = nama
    self.__sifat = sifat
    self.__ukuran = ukuran
    self.__jumlah_kaki = jumlah_kaki
  
  def showInfo(self):
    print(f'Nama\t\t: {self.__nama}\nSifat\t\t: {self.__sifat}\nUkuran\t\t: {self.__ukuran}\nJumlah Kaki\t: {self.__jumlah_kaki}')

class Mamalia(Animal):
  def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_jalan, jenis_mamalia):
    super().__init__(nama, sifat, ukuran, jumlah_kaki)
    self.__bisa_jalan = bisa_jalan
    self.__jenis_mamalia = jenis_mamalia

  def getBisaJalan(self):
    print(f'Bisa Jalan\t: {self.__bisa_jalan}')
  
  def getJenisMamalia(self):
    print(f'Jenis Mamalia\t: {self.__jenis_mamalia}')
  
  def getInfo(self):
    super().showInfo()
    self.getBisaJalan()  
    self.getJenisMamalia()  

class Aves(Animal):
  def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
    super().__init__(nama, sifat, ukuran, jumlah_kaki)
    self.__bisa_terbang = bisa_terbang
    self.__jenis_aves = jenis_aves

  def getBisaTerbang(self):
    print(f'Bisa Terbang\t: {self.__bisa_terbang}')
  
  def getJenisAves(self):
    print(f'Jenis Aves\t: {self.__jenis_aves}')
  
  def getInfo(self):
    super().showInfo()
    self.getBisaTerbang()  
    self.getJenisAves()  

class Merpati(Aves):
  def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
    super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)

class Ayam(Aves):
  def __init__(self, nama, sifat, ukuran, jumlah_kaki, jenis_ayam, bisa_diadu):
    super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang=True, jenis_aves=True) 
    self.__jenis_ayam = jenis_ayam
    self.__bisa_diadu = bisa_diadu

  def getJenisAyam(self):
    print(f'Jenis Ayam\t: {self.__jenis_ayam}')
  
  def getBisaDiadu(self):
    print(f'Bisa Diadu\t: {self.__bisa_diadu}')
  
  def getInfo(self):
    super().showInfo()
    self.getJenisAyam()  
    self.getBisaDiadu()  

# Objek Mamalia
objek_mamalia1 = Mamalia('Kucing', 'Jinak', 'Kecil', 4, True, 'Felidae')

# Objek Aves
objek_aves1 = Aves('Jalak', 'Jinak', 'Kecil', 2, True, 'Sturnidae')

# Objek Merpati
objek_merpati1 = Merpati('Merpati', 'Jinak', 'Kecil', 2, True, 'Columbiade')

# Objek Ayam
objek_ayam1 = Ayam('Ayam Cemani', 'Jinak', 'Kecil', 2, 'Phasianidae', True)

if __name__ == '__main__':
  objek_mamalia1.getInfo()
  print()
  objek_aves1.getInfo()
  print()
  objek_merpati1.getInfo()
  print()
  objek_ayam1.getInfo()
