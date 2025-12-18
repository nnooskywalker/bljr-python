# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++++3-------------10++++++++

inputuser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# ++++3---------------
# Memeriksa angka kurang dari 3
iskurangDari = (inputuser < 3)
print("Kurang dari 3= ", iskurangDari)

# ---------10++++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputuser > 10)
print("Lebih dari 10= ", isLebihDari)

# +++++++3-------------10++++++++
isCorrect = iskurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)



#---------3+++++++++++10--------------
# Kasus Irisan
print("\n",10*"=","\n")
inputuser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# -------3++++++++
# lebih dari 3
isLebihDari = inputuser > 3
print("Lebih dari 3= ",isLebihDari)

# +++++++++++10-----------
# kurang dari 10
iskurangDari = inputuser < 10
print("Kurang dari 10= ",iskurangDari)

#---------3+++++++++++10--------------
isCorrect = iskurangDari and isLebihDari
print("angka yang anda masukan: ", isCorrect)
