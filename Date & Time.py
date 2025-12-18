# Date and Time (latihan)

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)

tanggal = dt.date(2007,6,3)
print(tanggal)

print("Silahkan masukkan tanggal, bulan, dan tahun lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah {tanggal_lahir}")
print(f"Hari nya adalah : {tanggal_lahir:%A}")

tahun_ini = dt.date.today()
print(f"hari ini tanggal : {tahun_ini}")

umur_hari = tahun_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Umur anda sekarang adalah {umur_tahun} tahun")
print(f"umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan, {umur_hari} hari")






print(5*'-'+"HAPPY 18th BIRTHDAY ^_^"+5*'-')