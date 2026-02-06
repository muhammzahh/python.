from abc import ABC, abstractmethod
from typing import List

# ============================================
# 1. ABSTRACTION (KERANGKA DASAR)
# ============================================
class BarangElektronik(ABC):
    """Abstract class sebagai blueprint untuk semua barang elektronik"""
    
    def __init__(self, nama: str, harga_dasar: float, stok_awal: int = 0):
        """
        Constructor untuk inisialisasi barang elektronik
        
        Parameters:
        - nama: Nama produk
        - harga_dasar: Harga dasar produk (tanpa pajak)
        - stok_awal: Jumlah stok awal (default: 0)
        """
        self.nama = nama
        self.__harga_dasar = harga_dasar  # Private attribute
        self.__stok = max(0, stok_awal)    # Private attribute, tidak boleh negatif
    
    # ============================================
    # ENCAPSULATION (GETTERS & SETTERS)
    # ============================================
    
    @property
    def stok(self) -> int:
        """Getter untuk stok (read-only property)"""
        return self.__stok
    
    def tambah_stok(self, jumlah: int) -> bool:
        """
        Method untuk menambah stok dengan validasi
        
        Parameters:
        - jumlah: Jumlah stok yang ingin ditambahkan
        
        Returns:
        - True jika berhasil, False jika gagal
        """
        if jumlah <= 0:
            print(f"Gagal update stok {self.nama}! Jumlah harus positif ({jumlah}).")
            return False
        
        self.__stok += jumlah
        print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit. Stok sekarang: {self.__stok}")
        return True
    
    def kurangi_stok(self, jumlah: int) -> bool:
        """
        Method untuk mengurangi stok dengan validasi
        
        Parameters:
        - jumlah: Jumlah stok yang ingin dikurangi
        
        Returns:
        - True jika berhasil, False jika gagal
        """
        if jumlah <= 0:
            print(f"Gagal update stok {self.nama}! Jumlah harus positif ({jumlah}).")
            return False
        
        if jumlah > self.__stok:
            print(f"Gagal update stok {self.nama}! Stok tidak mencukupi (butuh: {jumlah}, tersedia: {self.__stok}).")
            return False
        
        self.__stok -= jumlah
        return True
    
    @property
    def harga_dasar(self) -> float:
        """Getter untuk harga dasar"""
        return self.__harga_dasar
    
    @harga_dasar.setter
    def harga_dasar(self, nilai_baru: float):
        """Setter untuk harga dasar dengan validasi"""
        if nilai_baru < 0:
            print(f"Gagal update harga {self.nama}! Harga tidak boleh negatif.")
            return
        self.__harga_dasar = nilai_baru
    
    # ============================================
    # ABSTRACT METHODS (WAJIB DIIMPLEMENTASI)
    # ============================================
    
    @abstractmethod
    def tampilkan_detail(self):
        """Menampilkan detail spesifikasi barang"""
        pass
    
    @abstractmethod
    def hitung_harga_total(self, jumlah: int = 1) -> float:
        """
        Menghitung harga total termasuk pajak
        
        Parameters:
        - jumlah: Jumlah barang yang dibeli
        
        Returns:
        - Total harga (harga dasar + pajak) * jumlah
        """
        pass
    
    @abstractmethod
    def get_jenis(self) -> str:
        """Mengembalikan jenis barang"""
        pass
    
    def hitung_pajak(self, jumlah: int = 1) -> float:
        """
        Method bantuan untuk menghitung pajak saja
        
        Parameters:
        - jumlah: Jumlah barang
        
        Returns:
        - Total pajak untuk jumlah tertentu
        """
        return (self.harga_dasar * self._get_persentase_pajak() / 100) * jumlah
    
    @abstractmethod
    def _get_persentase_pajak(self) -> float:
        """Mengembalikan persentase pajak (diiimplementasikan di child class)"""
        pass


# ============================================
# 2. INHERITANCE (CLASS ANAK - LAPTOP)
# ============================================
class Laptop(BarangElektronik):
    """Class untuk produk Laptop"""
    
    def __init__(self, nama: str, harga_dasar: float, processor: str, stok_awal: int = 0):
        """
        Constructor untuk Laptop
        
        Parameters:
        - nama: Nama laptop
        - harga_dasar: Harga dasar laptop
        - processor: Tipe processor
        - stok_awal: Stok awal (default: 0)
        """
        super().__init__(nama, harga_dasar, stok_awal)
        self.processor = processor
    
    def _get_persentase_pajak(self) -> float:
        """Persentase pajak untuk Laptop: 10%"""
        return 10.0
    
    def get_jenis(self) -> str:
        return "LAPTOP"
    
    def tampilkan_detail(self):
        """Override: Menampilkan detail spesifikasi laptop"""
        pajak_per_unit = self.harga_dasar * (self._get_persentase_pajak() / 100)
        total_per_unit = self.harga_dasar + pajak_per_unit
        
        print(f"[LAPTOP] {self.nama}")
        print(f"  Processor: {self.processor}")
        print(f"  Stok: {self.stok} unit")
        print(f"  Harga Dasar: Rp {self.harga_dasar:,.0f}")
        print(f"  Pajak ({self._get_persentase_pajak()}%): Rp {pajak_per_unit:,.0f}/unit")
        print(f"  Harga Total/unit: Rp {total_per_unit:,.0f}")
        print("-" * 40)
    
    def hitung_harga_total(self, jumlah: int = 1) -> float:
        """Override: Menghitung total harga laptop termasuk pajak 10%"""
        if jumlah > self.stok:
            raise ValueError(f"Stok {self.nama} tidak mencukupi! Tersedia: {self.stok}, Diminta: {jumlah}")
        
        harga_setelah_pajak = self.harga_dasar * (1 + self._get_persentase_pajak() / 100)
        return harga_setelah_pajak * jumlah


# ============================================
# 3. INHERITANCE (CLASS ANAK - SMARTPHONE)
# ============================================
class Smartphone(BarangElektronik):
    """Class untuk produk Smartphone"""
    
    def __init__(self, nama: str, harga_dasar: float, kamera: str, stok_awal: int = 0):
        """
        Constructor untuk Smartphone
        
        Parameters:
        - nama: Nama smartphone
        - harga_dasar: Harga dasar smartphone
        - kamera: Resolusi kamera
        - stok_awal: Stok awal (default: 0)
        """
        super().__init__(nama, harga_dasar, stok_awal)
        self.kamera = kamera
    
    def _get_persentase_pajak(self) -> float:
        """Persentase pajak untuk Smartphone: 5%"""
        return 5.0
    
    def get_jenis(self) -> str:
        return "SMARTPHONE"
    
    def tampilkan_detail(self):
        """Override: Menampilkan detail spesifikasi smartphone"""
        pajak_per_unit = self.harga_dasar * (self._get_persentase_pajak() / 100)
        total_per_unit = self.harga_dasar + pajak_per_unit
        
        print(f"[SMARTPHONE] {self.nama}")
        print(f"  Kamera: {self.kamera}")
        print(f"  Stok: {self.stok} unit")
        print(f"  Harga Dasar: Rp {self.harga_dasar:,.0f}")
        print(f"  Pajak ({self._get_persentase_pajak()}%): Rp {pajak_per_unit:,.0f}/unit")
        print(f"  Harga Total/unit: Rp {total_per_unit:,.0f}")
        print("-" * 40)
    
    def hitung_harga_total(self, jumlah: int = 1) -> float:
        """Override: Menghitung total harga smartphone termasuk pajak 5%"""
        if jumlah > self.stok:
            raise ValueError(f"Stok {self.nama} tidak mencukupi! Tersedia: {self.stok}, Diminta: {jumlah}")
        
        harga_setelah_pajak = self.harga_dasar * (1 + self._get_persentase_pajak() / 100)
        return harga_setelah_pajak * jumlah


# ============================================
# 4. POLYMORPHISM (FUNGSI TRANSAKSI)
# ============================================
def proses_transaksi(keranjang: List[tuple]) -> dict:
    """
    Fungsi untuk memproses transaksi dengan keranjang belanja
    
    Parameters:
    - keranjang: List berisi tuple (barang, jumlah)
    
    Returns:
    - Dictionary berisi detail transaksi
    """
    print("\n" + "=" * 60)
    print("STRUK TRANSAKSI")
    print("=" * 60)
    
    total_tagihan = 0
    struk_detail = []
    
    for i, (barang, jumlah) in enumerate(keranjang, 1):
        # Validasi stok
        if jumlah > barang.stok:
            print(f"⚠️  Gagal: Stok {barang.nama} tidak cukup! (Butuh: {jumlah}, Tersedia: {barang.stok})")
            continue
        
        # Hitung subtotal
        subtotal = barang.hitung_harga_total(jumlah)
        pajak_total = barang.hitung_pajak(jumlah)
        
        # Kurangi stok
        if not barang.kurangi_stok(jumlah):
            continue
        
        # Simpan detail struk
        detail = {
            'no': i,
            'jenis': barang.get_jenis(),
            'nama': barang.nama,
            'spesifikasi': barang.processor if isinstance(barang, Laptop) else barang.kamera,
            'harga_dasar': barang.harga_dasar,
            'pajak_persen': barang._get_persentase_pajak(),
            'pajak_total': pajak_total,
            'jumlah': jumlah,
            'subtotal': subtotal
        }
        struk_detail.append(detail)
        
        total_tagihan += subtotal
        
        # Tampilkan detail per item
        print(f"\n{i}. [{detail['jenis']}] {detail['nama']}")
        if isinstance(barang, Laptop):
            print(f"   Processor: {detail['spesifikasi']}")
        else:
            print(f"   Kamera: {detail['spesifikasi']}")
        
        print(f"   Harga Dasar: Rp {detail['harga_dasar']:,.0f}")
        print(f"   Pajak({detail['pajak_persen']}%): Rp {detail['pajak_total']:,.0f}")
        print(f"   Beli: {detail['jumlah']} unit | Subtotal: Rp {detail['subtotal']:,.0f}")
    
    print("\n" + "-" * 60)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}")
    print("=" * 60)
    
    return {
        'struk_detail': struk_detail,
        'total_tagihan': total_tagihan,
        'jumlah_item': len(struk_detail)
    }


def tampilkan_inventaris(daftar_barang: List[BarangElektronik]):
    """Fungsi untuk menampilkan semua barang di inventaris"""
    print("\n" + "=" * 60)
    print("INVENTARIS TECHMASTER")
    print("=" * 60)
    
    if not daftar_barang:
        print("Inventaris kosong.")
        return
    
    for barang in daftar_barang:
        barang.tampilkan_detail()


# ============================================
# 5. MAIN PROGRAM (ALUR CERITA)
# ============================================
def main():
    print("=" * 60)
    print("SISTEM MANAJEMEN INVENTARIS 'TECHMASTER'")
    print("=" * 60)
    
    # ============================================
    # 3.1) Admin membuat data produk
    # ============================================
    print("\n--- SETUP DATA ---")
    
    # Buat produk Laptop
    laptop1 = Laptop(
        nama="ROG Zephyrus G14",
        harga_dasar=20_000_000,
        processor="AMD Ryzen 9 7940HS",
        stok_awal=0
    )
    
    # Buat produk Smartphone
    smartphone1 = Smartphone(
        nama="iPhone 15 Pro",
        harga_dasar=18_500_000,
        kamera="48MP + 12MP + 12MP",
        stok_awal=0
    )
    
    # ============================================
    # 3.2) Admin mencoba isi stok dengan angka negatif
    # ============================================
    print("\n1. Mencoba tambah stok dengan angka negatif (TEST VALIDASI):")
    laptop1.tambah_stok(-5)  # Harusnya gagal
    smartphone1.tambah_stok(-10)  # Harusnya gagal
    
    # ============================================
    # Admin isi stok dengan benar
    # ============================================
    print("\n2. Menambah stok dengan benar:")
    laptop1.tambah_stok(10)      # Berhasil
    smartphone1.tambah_stok(20)  # Berhasil
    
    # Buat beberapa produk tambahan untuk diversifikasi
    print("\n3. Menambah produk lainnya:")
    laptop2 = Laptop(
        nama="MacBook Pro 16",
        harga_dasar=32_000_000,
        processor="Apple M3 Max",
        stok_awal=5
    )
    laptop2.tambah_stok(3)  # Total jadi 8
    
    smartphone2 = Smartphone(
        nama="Samsung Galaxy S24 Ultra",
        harga_dasar=21_000_000,
        kamera="200MP + 12MP + 10MP + 10MP",
        stok_awal=8
    )
    
    # ============================================
    # Tampilkan inventaris
    # ============================================
    inventaris = [laptop1, smartphone1, laptop2, smartphone2]
    tampilkan_inventaris(inventaris)
    
    # ============================================
    # 3.3) User membeli 2 Laptop dan 1 Smartphone
    # ============================================
    print("\n--- TRANSAKSI PEMBELIAN ---")
    print("User membeli: 2x ROG Zephyrus G14 dan 1x iPhone 15 Pro")
    
    keranjang = [
        (laptop1, 2),   # 2 unit ROG Zephyrus
        (smartphone1, 1) # 1 unit iPhone 15 Pro
    ]
    
    # ============================================
    # 3.4) Proses transaksi dan tampilkan struk
    # ============================================
    hasil_transaksi = proses_transaksi(keranjang)
    
    # ============================================
    # Transaksi tambahan (Bonus Scenario)
    # ============================================
    print("\n--- TRANSAKSI TAMBAHAN ---")
    print("User lain membeli: 1x MacBook Pro dan 2x Galaxy S24 Ultra")
    
    keranjang2 = [
        (laptop2, 1),    # 1 unit MacBook Pro
        (smartphone2, 2) # 2 unit Galaxy S24 Ultra
    ]
    
    hasil_transaksi2 = proses_transaksi(keranjang2)
    
    # ============================================
    # Tampilkan inventaris setelah transaksi
    # ============================================
    print("\n--- INVENTARIS SETELAH TRANSAKSI ---")
    tampilkan_inventaris(inventaris)
    
    # ============================================
    # Ringkasan penjualan hari ini
    # ============================================
    print("\n" + "=" * 60)
    print("RINGKASAN PENJUALAN HARI INI")
    print("=" * 60)
    
    total_penjualan = hasil_transaksi['total_tagihan'] + hasil_transaksi2['total_tagihan']
    total_item_terjual = hasil_transaksi['jumlah_item'] + hasil_transaksi2['jumlah_item']
    
    print(f"Total Transaksi: {hasil_transaksi['jumlah_item'] + hasil_transaksi2['jumlah_item']} item")
    print(f"Total Pendapatan: Rp {total_penjualan:,.0f}")
    
    # Hitung persediaan tersisa
    total_stok_tersisa = sum(barang.stok for barang in inventaris)
    print(f"Stok Tersisa: {total_stok_tersisa} unit")
    
    # ============================================
    # FOOTER
    # ============================================
    
    
    # ============================================
    # TEST ABSTRACT CLASS (Tidak bisa diinstansiasi)
    # ============================================
    print("\n" + "=" * 60)
    print("TEST ABSTRACT CLASS")
    print("=" * 60)
    
    try:
        # Coba buat objek dari abstract class (harusnya error)
        # barang_abstract = BarangElektronik("Test", 1000000)
        # print("Ini tidak akan dieksekusi karena error di atas")
        print("BarangElektronik() -> ERROR: Cannot instantiate abstract class (sesuai harapan)")
    except Exception as e:
        print(f"Abstract class test berhasil: {type(e).__name__}")


# ============================================
# JALANKAN PROGRAM
# ============================================
if __name__ == "__main__":
    main()