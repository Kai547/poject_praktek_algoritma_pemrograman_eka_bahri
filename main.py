#masukkan jumlah mahasiswa
a = int(input('masukkan jumlah :'))
#input nilai
total_nilai = 0
#format

for n in range(a):
    nilai = float(input(f'Nilai mahasiswa ke-{n+1} :'))
    total_nilai += nilai

#hitung rata rata

b= total_nilai / a 

print(f"rata-rata Nilai : {b}")

#cek Kelulusan 

if b >= 90 :
    print('lulus')

else:
    print('tidak lulus')

#masukkan jumlah mahasiswa
a = int(input('masukkan jumlah :'))
#input nilai
total_nilai = 0
#format

for n in range(a):
    nilai = float(input(f'Nilai mahasiswa ke-{n+1} :'))
    total_nilai += nilai

#hitung rata rata

b= total_nilai / a 

print(f"rata-rata Nilai : {b}")

#cek Kelulusan 

if b >= 90 :
    print('lulus')

else:
    print('tidak lulus')

