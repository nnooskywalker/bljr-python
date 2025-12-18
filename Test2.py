# (1) -------0++++++++5--------8++++++++11---------

'''
print("(1) --------0++++++++5-------8++++++++11-------")

inputuser = (float(input("Masukan angka: ")))

lebihdari_0 = (inputuser > 0)
kurangdari_5 = (inputuser < 5)

lebihdari_8 = (inputuser > 8)
kurangdari_11 = (inputuser < 11)

input1 = lebihdari_0 and kurangdari_5

input2 = lebihdari_8 and kurangdari_11

input1_and_input2 = input1 or input2

print("Angka yang anda masukkan= ", input1_and_input2)

print(" ==================================== ")
print("(2) ++++++0-------5+++++8--------11++++++")

inputuser = (float(input("Masukkan Angka: ")))

kurangdari_0 = (inputuser < 0)

lebihdari_5 = (inputuser > 5)
kurangdari_8 = (inputuser < 8)
lebihdari_11 = (inputuser > 11)

input1 = kurangdari_0 or lebihdari_5
input2 = kurangdari_8 or lebihdari_11

inputtotal = input1 and input2

print("Angka yang anda masukkan= ", inputtotal)

a = 2
print("bilangan :", a, "binary: ", format(a,'05b'))

'''
'''
angka = int(input("Masukkan angka: "))
_1 = (angka < -1)
_2 = (angka > 5)

input_ = _1 or _2

print(angka , "< -1" , " = " , _1)
print(angka, ">  5", " = ", _2)
print('Angka yang anda masukkan : ',input_)

#a = f"angka yang anda masukkan adalah {input_}"
#b = f"{angka} < -1 = {_1}"
#print(a)
#print(b)'
'''
'''
print(6*'='+"DM by Instagram"+6*'=')

print(f"AI : DOMISILI MANA ?")
chat_1 = input("Nino : ")

if chat_1=="jkt" :
         print(f"AI : JAUH\n\t\bAKU JATIM")
elif chat_1=="sby" :
        print(f"AI : JAUH \nAKU BANDUNG")
chat_2 = input("Nino: ")

if chat_2=="btw fontnya kok bisa gitu? apa ga pusing" :
        print(f"AI : PUSING KENAPA ? \n\tHAHAHA MALAH KELIATAN JELAS")'
'''

#### PR : buat belah ketupat
'''
sisi = 10
count = 1
spasi = int(sisi / 2)
while True :
        print(" "*spasi,"*"*count)
        count+=1
        spasi -=1

        if count > sisi :
                break

        else :
            count +=1 
            continue

while True :
       print(" "*spasi,"*"*count)
       count -=1
       spasi +=1

       else :
         count -=1
       
       if count == 0 : 
              break
  '''

angka = int(input("Masukkan angka:"))

x = angka % 2

if x == 1 : 
        print("Angka yang anda masukkan adalah angka Ganjil")

elif x == 0 :
        print("Genap")



       
          

        






         


