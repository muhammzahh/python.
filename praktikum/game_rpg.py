# Parent Class (Base Class)
class Hero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print(f"{self.nama} (Hero) menyerang dengan tangan kosong.")

    def info(self):
        print(f"{self.nama} adalah seorang Hero")


# Child Class 1 - Mage
class Mage(Hero):
    def __init__(self, nama, mana=100):
        super().__init__(nama)
        self.mana = mana
    
    def serang(self):
        if self.mana >= 20:
            print(f"{self.nama} (Mage) menembakkan Bola Api! Boom! 🔥")
            self.mana -= 20
        else:
            print(f"{self.nama} (Mage) gagal serang! Mana habis. 😫")
    
    def info(self):
        print(f"{self.nama} adalah Mage | Mana: {self.mana}")


# Child Class 2 - Archer
class Archer(Hero):
    def __init__(self, nama, arrows=30):
        super().__init__(nama)
        self.arrows = arrows
    
    def serang(self):
        if self.arrows > 0:
            print(f"{self.nama} (Archer) memanah dari jauh! Jleb! 🏹")
            self.arrows -= 1
        else:
            print(f"{self.nama} (Archer) tidak punya anak panah! 🏹❌")
    
    def info(self):
        print(f"{self.nama} adalah Archer | Anak panah: {self.arrows}")


# Child Class 3 - Fighter
class Fighter(Hero):
    def __init__(self, nama, stamina=100):
        super().__init__(nama)
        self.stamina = stamina
    
    def serang(self):
        if self.stamina >= 15:
            print(f"{self.nama} (Fighter) memukul dengan pedang! Slash! ⚔️")
            self.stamina -= 15
        else:
            print(f"{self.nama} (Fighter) terlalu lelah! 💤")
    
    def info(self):
        print(f"{self.nama} adalah Fighter | Stamina: {self.stamina}")


# Child Class 4 - Healer (Bonus)
class Healer(Hero):
    def __init__(self, nama, healing_power=50):
        super().__init__(nama)
        self.healing_power = healing_power
    
    def serang(self):
        print(f"{self.nama} (Healer) mengeluarkan sinyal penyembuhan! 💚")
        print("  'Aku di sini untuk membantu, bukan melukai!'")
    
    def sembuhkan(self, target):
        print(f"{self.nama} menyembuhkan {target.nama} sebesar {self.healing_power} HP 💚")
    
    def info(self):
        print(f"{self.nama} adalah Healer | Healing Power: {self.healing_power}")


# ============================================
# PENERAPAN POLYMORPHISM
# ============================================

print("=" * 60)
print("PRAKTIKUM 6: POLYMORPHISM")
print("=" * 60)

# Kita punya daftar hero campuran
pasukan = [
    Mage("Eudora", mana=80),
    Archer("Miya", arrows=25),
    Fighter("Zilong", stamina=90),
    Mage("Gord", mana=120),
    Archer("Lesley", arrows=10),
    Fighter("Alucard", stamina=30),
    Healer("Rafaela"),
    Mage("Kagura"),
]

print("\n=== INFO PASUKAN ===")
for pahlawan in pasukan:
    pahlawan.info()

print("\n" + "=" * 40)
print("--- PERANG DIMULAI ---")
print("=" * 40)

# POLYMORPHISM: Satu perintah loop, tapi respon berbeda-beda
print("\n SEMUA HERO MENYERANG (RONDE 1):")
for pahlawan in pasukan:
    pahlawan.serang()  # Setiap class punya implementasi serang() berbeda

print("\n SEMUA HERO MENYERANG (RONDE 2):")
for pahlawan in pasukan:
    pahlawan.serang()  # Perhatikan perubahan (mana/arrows berkurang)

print("\n SEMUA HERO MENYERANG (RONDE 3):")
for pahlawan in pasukan:
    pahlawan.serang()  # Beberapa akan gagal karena resource habis

# ============================================
# DEMONSTRASI POLYMORPHISM LAINNYA
# ============================================

print("\n" + "=" * 40)
print("DEMONSTRASI POLYMORPHISM LAINNYA")
print("=" * 40)

# Contoh 1: List dengan tipe berbeda tapi bisa diproses sama
print("\n1. MENGGUNAKAN LOOP DENGAN BERBAGAI TIPE:")
heroes = [Mage("Harith"), Archer("Clint"), Fighter("Freya"), Healer("Estes")]

for hero in heroes:
    # Meski tipe berbeda, semua punya method serang() dan info()
    print(f"\n{hero.__class__.__name__}: ", end="")
    hero.serang()

# Contoh 2: Function yang menerima berbagai tipe Hero
print("\n\n2. FUNCTION YANG MENERIMA BERBAGAI TIPE HERO:")
def latihan_perang(karakter):
    """Function ini bisa terima Hero apapun karena semua punya serang()"""
    print(f"🛡️ {karakter.nama} sedang berlatih...")
    karakter.serang()
    print(f"  Latihan selesai!\n")

# Panggil function dengan berbagai tipe hero
latihan_perang(Mage("Valir"))
latihan_perang(Archer("Wanwan"))
latihan_perang(Fighter("Thamuz"))

# Contoh 3: Polymorphism dengan isinstance()
print("\n3. MENGELOMPOKKAN HERO BERDASARKAN TIPE:")
# Buat pasukan campuran lagi
campuran = [Mage("Alice"), Archer("Bob"), Fighter("Charlie"), Mage("David"), Healer("Eve")]

mage_count = 0
archer_count = 0
fighter_count = 0
healer_count = 0

for hero in campuran:
    if isinstance(hero, Mage):
        mage_count += 1
    elif isinstance(hero, Archer):
        archer_count += 1
    elif isinstance(hero, Fighter):
        fighter_count += 1
    elif isinstance(hero, Healer):
        healer_count += 1

print(f"📊 Komposisi Pasukan:")
print(f"  Mage: {mage_count} orang")
print(f"  Archer: {archer_count} orang")  
print(f"  Fighter: {fighter_count} orang")
print(f"  Healer: {healer_count} orang")

# Contoh 4: Polymorphism dalam dictionary
print("\n4. POLYMORPHISM DALAM DICTIONARY:")
hero_dict = {
    "mage1": Mage("Lunox"),
    "archer1": Archer("Popol"),
    "fighter1": Fighter("Yu Zhong"),
    "healer1": Healer("Angela")
}

print("Memanggil hero dari dictionary:")
for key, hero in hero_dict.items():
    print(f"  {key}: ", end="")
    hero.serang()

# ============================================
# PERANG BESAR (FINAL BATTLE)
# ============================================

print("\n" + "=" * 50)
print("⚔️  PERANG BESAR - FINAL BATTLE ⚔️")
print("=" * 50)

# Buat dua pasukan
pasukan_merah = [Mage("Eudora"), Archer("Miya"), Fighter("Zilong")]
pasukan_biru = [Mage("Gord"), Archer("Lesley"), Fighter("Alucard")]

print("\n🎌 PASUKAN MERAH:")
for hero in pasukan_merah:
    hero.info()

print("\n🎌 PASUKAN BIRU:")
for hero in pasukan_biru:
    hero.info()

print("\n⚔️  PERTEMPURAN DIMULAI!")
ronde = 1
while len(pasukan_merah) > 0 and len(pasukan_biru) > 0:
    print(f"\n--- RONDE {ronde} ---")
    
    # Setiap hero di pasukan merah menyerang
    print("Pasukan Merah menyerang:")
    for hero in pasukan_merah[:]:  # Copy list untuk iterasi aman
        if len(pasukan_biru) > 0:
            target = pasukan_biru[0]
            print(f"  ", end="")
            hero.serang()
    
    # Setiap hero di pasukan biru menyerang  
    print("\nPasukan Biru menyerang:")
    for hero in pasukan_biru[:]:
        if len(pasukan_merah) > 0:
            target = pasukan_merah[0]
            print(f"  ", end="")
            hero.serang()
    
    ronde += 1
    if ronde > 5:  # Mencegah infinite loop
        break

# ============================================

