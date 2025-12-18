print(10*"-"+"Rata-Rata Nilai Rapot"+10*"-")

kls10_1 = input("masukkan nilai :")
kls10_2 = input("masukkan nilai :")
kls11_1 = input("masukkan nilai :")
kls11_2 = input("masukkan nilai :")
kls12_1 = input("masukkan nilai :")

rata_2 = (kls10_1 + kls10_2 + kls11_1 + kls11_2 + kls12_1) / 5

print(f"rata-rata anda adalah {rata_2})

if rata_2 >= 80 :
          print("aman untuk masuk eligible")
          
elif rata_2 <= 80 :
          print("anda tidak masuk eligible")
          
print(5*"="+"TERIMA KASIH"+5*"=")