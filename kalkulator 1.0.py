# Kalkulator sederhana
print(15*'=')
print("Kalkulator Sederhana")
print(15*'=')

angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("masukkan angka 2 = "))

# cabang
if operator == "+":
            print(f"= {angka_1+angka_2}")

elif operator == "-":
            print(f"= {angka_1-angka_2}")

elif operator == "x" or operator == "*":
            print(f"= {angka_1*angka_2}")
        
elif operator == "/":
            print(f"= {angka_1/angka_2}")
else :
        print('Error')

print("Terima kasih telah menggunakan kalkulator ^_^")
