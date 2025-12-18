print("\nKONVERSI SUHU SEDERHANA\n")
print("Made by Nino 20/03/2025 20:28")
print("5*'-'+FAHRENHEIT+5*'-'")

Fahrenheit = float(input("Fahrenheit: "))

print("suhu dalam fahrenheit adalah ", Fahrenheit, "fahrenheit")
# Fahrenheit to Kelvin
kelvin = (5/9) * (Fahrenheit-32) + 273

print("suhu dalam kelvin adalah ", kelvin, "kelvin")

print("---------------------KELVIN-------------------")
kelvin = float(input("Kelvin: "))
print("suhu dalam kelvin adalah", kelvin)

#Kelvin to fahrenheit
Fahrenheit = (9/5) * (kelvin-273) + 32
print("suhu dalam fahrenheit adalah ", Fahrenheit, "fahrenheit")