#################################### Cara Kerja ############################

## """comment multiline"""
#kita bisa mengcompile python ke yang namanya bytecode 
# cara mengcompile, buka terminal dan tuliskan python -m py_compile Main.py

############### Operasi Aritmatika ##############
a=10
b=3

#Operasi penjumlahan (+)
hasil= a + b
print(a,'+',b,'=',hasil)

#operasi pengurangan (-)
hasil= a - b
print(a,'-',b,'=',hasil)

#operasi perkalian (*)
hasil= a * b
print(a,'*',b,'=',hasil)

#operasi pembagian (/)
hasil= a / b
print(a,'/',b,'=',hasil)

#operasi eksponen (pangkat) (**)
hasil = a ** b
print(a,'**',b,'=',hasil)

#operasi modulus (sisa pembagian) (%)
hasil = a % b
print(a,'%',b,'=',hasil)

#operasi floor division (pembulatan pembagian) (//)
hasil = a // b
print(a, '//', b, '=', hasil)

#prioritas operasi (operational presidence)
''''
   1. ()'
   2. eksponen **'
   3. perkalian dan teman-teman * / ** % //
   4. pertambahan dan pengurangan + -
'''

x=3
y=2
z=4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)

# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=', hasil)