# Latihan
print("Nama : Assandra Julyant Firdausy")
print("NIM  : 312210384")

daftarkontak = {"Nama": "Nomer Telepon"}
kontak = {'Agung': '081267888', 'Darto': '087677776'}

# print
print("============================")
print("|   # Nama   |Nomor Telepon|")
print("============================")
print("|   # Agung    |  ", kontak['Agung'], '|')
print("|   # Darto   |  ", kontak['Darto'], '|')
print("============================")
print()

# Tampilkan kontaknya Agung
print("# Tampilkan kontaknya Agung")
print("===========================")
print("|    Agung     | ", kontak['Agung'], '|')
print("===========================")
print()

# Tambah kontak baru dengan nama Roko, nomor 087654544
print("# Tambah kontak baru dengan nama Roko, nomor 087654544")
kontak['Roko'] = '087654544'
print("===========================")
print("|    Roko    | ", kontak['Roko'], '|')
print("===========================")
print()

# Ubah kontak Darto dengan nomor baru 088999776
print("# Ubah kontak Darto dengan nomor baru 088999776")
kontak['Darto'] = '088999776'
print("===========================")
print("|    Darto    | ", kontak['Darto'], '|')
print("===========================")
print()

# Tampilkan semua Nama
print("# Tampilkan semua Nama")
print("==================================")
print(kontak.keys())
print("==================================")
print()

# Tampilkan semua Nomor
print("# Tampilkan semua Nomor")
print("====================================================")
print(kontak.values())
print("====================================================")
print()

# Tampilkan daftar Nama dan nomornya
print("# Tampilkan daftar Nama dan nomornya")
print("================================================================================")
print(kontak.items())
print("================================================================================")
print()

# Menghapus kontak Darto
print("# Hapus kontak Darto")
print("=========================================================")
kontak.pop('Darto')
print(kontak.items())
print("=========================================================")