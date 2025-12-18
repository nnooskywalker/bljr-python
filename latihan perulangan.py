# Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan for

## dummy variable
print("awal For")

count = 1
for i in range(sisi):
    print("*"*count)

    count+=1


print("akhir dari For")

# 2. Menggunakan while

count = 1
print(20*'=')

print("awal While")
while True: 
          print("*"*count)
          count+=1

          if count > sisi:
                 break

print("akhir dari while")

print(20*'=')

# 3. hanya ganjil saja
count = 1
while True: 
        if (count%2):
          # print jika ganjil
          print("*"*count)
          count+=1
        else:
           # akan kembali ke atas jika ganjil
           count += 1
           continue

        # akan break jika count melebihi sisi
        if count > sisi:
                 break

print(20*'=')
        
# 4. segitiga sama sisi
count = 1
spasi = int(sisi/2)
while True: 
        if (count%2):
          # print jika ganjil
          print(" "*spasi,"+"*count)
          spasi -=1
          count +=1
        else:
           # akan kembali ke atas jika ganjil
           count += 1
           continue

        # akan break jika count melebihi sisi
        if count > sisi:
                 break