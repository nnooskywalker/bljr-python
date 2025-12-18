# continue, pass, break

## pass -> berfungsi sebagai dummy (tidak akan dieksekusi)
print(20*'='+'PASS'+20*'=')


angka = 0

while angka < 5:
    angka +=1

    if angka == 3:
        pass # ini tidak akan dieksekusi
    print(angka)

print(20*'='+'CONTINUE'+20*'=')


## continue
angka = 0
print(f"angka sekarang {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1
    

    if angka == 3:
        print("nice!")
        continue # akan membuat loop meloncat ke step selanjutnya

    print(f"whassupp") # aksi 2


print("Finish")

print(20*'='+'BREAK'+20*'=')

## Break
print("-----contoh 1-----")
# contoh 1
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") 
    

    if angka == 3:
        print("nice!")
        break

    print(f"whassupp") 

print("cukupp !")

print("-----contoh 2-----")
# contoh 2
data_int = int(input("Hitung sampai = "))

angka = 0

while True :
    angka += 1
    print(f"count -> {angka}")

    if angka == data_int :
        print("nice!")
        break

    print("wassupp")

print("finished")