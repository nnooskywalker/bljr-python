#################################### Cara Kerja ############################

## """comment multiline"""
#kita bisa mengcompile python ke yang namanya bytecode 
# cara mengcompile, buka terminal dan tuliskan python -m py_compile Main.py

#############################Input User##############################

#data yang dimasukkan pasti string
data = input("Masukkan Nama : ")

print("data= ",data,",type =", type(data))

#Mengubah ke int atau float, maka pakai casting
angka = int(input("Masukkan angka: "))
angka = float(input("Masukkan angka: "))

print("data= ", angka, "type= ", type(angka))

#Mengubah ke boolean
biner = bool(int(input("Masukkan nilai boolean =")))

print("data= ", biner, "type= ", type(biner))