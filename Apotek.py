print("=" * 60)
print("       APOTEK SEHAT SEJAHTERA - KONTROL STOK OBAT")
print("=" * 60)

stok_obat = {
    1: {"nama": "Paracetamol", "stok": 50, "harga": 5000},
    2: {"nama": "Amoxicillin", "stok": 15, "harga": 12000},
    3: {"nama": "Ibuprofen", "stok": 0, "harga": 8000},
    4: {"nama": "Omeprazole", "stok": 30, "harga": 15000},
    5: {"nama": "Vitamin C", "stok": 100, "harga": 20000},
    6: {"nama": "Cetirizine", "stok": 25, "harga": 6000},
    7: {"nama": "Metformin", "stok": 40, "harga": 10000},
    8: {"nama": "Amlodipine", "stok": 20, "harga": 7000},
    9: {"nama": "Salbutamol", "stok": 8, "harga": 25000},
    10: {"nama": "Antasida", "stok": 5, "harga": 9000},
}

print("\n--- DAFTAR 10 JENIS OBAT APOTEK ---")
for id_obat, info in stok_obat.items():
  status_ketersediaan = info["stok"] > 0
  ket = "Tersedia" if status_ketersediaan else "HABIS"
  print(
      f"{id_obat}. {info['nama']} | Stok: {info['stok']} unit | Rp"
      f" {info['harga']:,} [{ket}]".replace(",", ".")
  )

print("-" * 60)
nama_pembeli = input("Masukkan Nama Pembeli\t\t: ")
print(nama_pembeli)

try:
  pilihan = int(input("Pilih nomor obat yang ingin dibeli (1-10): "))
  print(pilihan)
  jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli\t: "))
  print(jumlah_beli)
except ValueError:
  pilihan = 0
  jumlah_beli = 0

print("\n" + "=" * 60)
print("              STRUK HASIL PEMBANDINGAN & TRANSAKSI")
print("=" * 60)

if pilihan in stok_obat:
  obat_dipilih = stok_obat[pilihan]
  nama_obat = obat_dipilih["nama"]
  stok_gudang = obat_dipilih["stok"]
  harga_satuan = obat_dipilih["harga"]

  print(f"Pelanggan        : {nama_pembeli}")
  print(f"Obat Diminta     : {nama_obat} ({jumlah_beli} unit)")
  print("-" * 60)

  if stok_gudang == 0:
    print(
        f"Hasil Pengecekan : [False] Stok {nama_obat} kosong (0 unit)."
        "\nStatus Transaksi : DITOLAK."
    )

  elif jumlah_beli <= stok_gudang:
    total_harga = jumlah_beli * harga_satuan
    sisa_stok = stok_gudang - jumlah_beli

    BATAS_AMAN = 10
    peringatan_stok = sisa_stok <= BATAS_AMAN

    print(f"Hasil Pengecekan : [True] Jumlah beli <= Stok gudang.")
    print(f"Status Transaksi : BERHASIL")
    print(f"Sisa Stok Gudang : {sisa_stok} unit")
    print(f"Total Bayar      : Rp {total_harga:,}".replace(",", "."))

    if peringatan_stok:
      print(
          "Peringatan Sistem: [True] Stok menipis! Sisa stok di bawah batas"
          f" aman ({BATAS_AMAN} unit)."
      )
    else:
      print(
          "Peringatan Sistem: [False] Stok masih berada di atas batas aman."
      )

  else:
    print(
        f"Hasil Pengecekan : [False] Permintaan ({jumlah_beli}) > Stok tersedia"
        f" ({stok_gudang})."
    )
    print("Status Transaksi : DITOLAK. Jumlah melebihi stok gudang.")

else:
  print("Status Transaksi : ERROR. Nomor obat yang dimasukkan tidak terdaftar.")

print("=" * 60)
