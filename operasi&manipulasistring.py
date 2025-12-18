# Operasi dan manipulasi string

# 1. Menyambung string (concatenate)
nama_pertama = "Reyhan"
nama_tengah = "Nino"
nama_akhir = "Aliffano"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

Nino = "Nino"
status = Nino in nama_lengkap
print( Nino + " ada di " + nama_lengkap + " = " + str(status))

nnooskywalker = "nnooskywalker"
status = nnooskywalker not in nama_lengkap
print(nnooskywalker + " tidak ada di " + nama_lengkap + " = " + str(status)) 

# mengulang string
print("wk"*10)
print(15* "wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-7 : " + nama_lengkap[7])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-(0:3) : " + nama_lengkap[0:4])
print("index ke-(0,2,4,6,8,10) : " + nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII CODE untuk spasi adalah " + str(ascii_code))

data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")

print("jumlah o pada " + data + " = " + str(jumlah))

#==========================PART 2====================================

## merubah case dari string

# merubah semua ke upper case (huruf kapital)

salam = "bro!"
print("Normal= ", salam)
salam = salam.upper()
print("upper= ", salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieZzzzzZZ"
print("Normal= ", alay)
alay= alay.lower()
print("lower= ",alay)

# pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam + " is lower = " + str(apakah_lower))

# contoh pengecekan upper case
apakah_upper = salam.isupper() #hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <--- untuk mengecek semuanya huruf
# isalnum() <--- huruf dan angka
# isdecimal() <--- angka saja
# isspace() <--- spasi, tab, newline \n
# istittle() <--- semua kata dimulai dengan huruf besar

judul = "Is Okay No To Be Orkay"
cek_judul = judul.istitle() #hasil bool

print(judul + " is tittle = " + str(cek_judul))

## ngecek komponen startswith() endswith ()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start= " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end= " + str(cek_end))

## penggabungan komponen join() dan split()
pisah = ['aku', 'saya', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = "akuehmsayaehmkamu"
print(gabungan.split('ehm'))

## alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikannya --> strip()
tengah = tengah.strip("-")
print("'"+tengah+"'")
