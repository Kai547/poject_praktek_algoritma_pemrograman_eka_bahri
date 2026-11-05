# 1. Input nilai tugas, UTS, UAS, dan kehadiran mahasiswa
nilai_tugas = float(input("Masukkan nilai Tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))
kehadiran = float(
    input("Masukkan persentase Kehadiran (contoh 85 untuk 85%): ")
)

# 2. Hitung Nilai Akhir
nilai_akhir = (
    (0.20 * nilai_tugas) + (0.30 * nilai_uts) + (0.50 * nilai_uas)
)

print("-" * 40)
print(f"Nilai Akhir: {nilai_akhir}")
print(f"Kehadiran  :{kehadiran}%")
print("-" * 40)

# Cek apakah nilai akhir genap (menggunakan modulus %)
is_genap = (nilai_akhir % 2) == 0

# Evaluasi Status Kelulusan
# 4. Status LULUS DENGAN PREDIKAT
if nilai_akhir >= 85 and kehadiran >= 90 and is_genap:
    status = "LULUS DENGAN PREDIKAT"

# 3 & 6. Status LULUS (tanpa predikat)
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"

# 5. Status BELUM LULUS
else:
    status = "BELUM LULUS"

# Tampilkan Status
print(f"Status Mahasiswa: {status}")


