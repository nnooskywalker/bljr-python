# Reyhan Nino
'''
print("\tLatihan String")
print("-------Menyambung string--------")
# Menyambung string
nama_awal = "Reyhan"
nama_akhir = "Nino"

nama_lengkap = nama_awal + " " + nama_akhir
print(nama_lengkap)

print("-------Panjang string--------")
# Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang string adalah: " + str(panjang))

print("---------Komponen string--------")

Rey = "Reyhan"
checking = Rey in nama_lengkap
print(Rey + " " + "ada di" + " " + nama_lengkap + " = " + str(checking) )

Aliff = "Aliffano"
checking = Aliff not in nama_lengkap
print(Aliff + " " + "tidak ada di" + " " + nama_lengkap + " = " + str(checking) )

print("---------Mengulang string--------")
print("Ha"*5)

print("-------------Indexing---------------")

print("Index ke 5 adalah ", nama_lengkap[5])
print("Index ke -3 adalah ", nama_lengkap[-3])

print("--------Huruf paling besar dan paling kecil---------")
print("Huruf terbesar adalah ", max(nama_lengkap))
print("Huruf terkecil adalah ", min(nama_lengkap))


print("-------------Asci code---------------")

ascicode = ord("n")
print("Asci code huruf n adalah ", str(ascicode))

data = 100
print("Huruf ke 100 adalah", chr(data))

#print("Banyak huruf a pada" + " " + Name + " adalah " + str(data))


'''
print(10*"-"+"Rata-Rata Nilai Rapot"+10*"-")

kls10_1 = float(input("kelas 10 semester 1 :"))
kls10_2 = float(input("kelas 10 semester 2 :"))
kls11_1 = float(input("kelas 11 semester 1 :"))
kls11_2 = float(input("kelas 11 semester 2 :"))
kls12_1 = float(input("kelas 12 semester 1 :"))

rata_2 = (kls10_1 + kls10_2 + kls11_1 + kls11_2 + kls12_1)/5

print(f"rata-rata anda adalah {rata_2}")

if rata_2 >= 80 :
          print("aman untuk masuk eligible")
          
elif rata_2 <= 80 :
          print("anda tidak masuk eligible")
          
print(5*"="+"TERIMA KASIH"+5*"=")

