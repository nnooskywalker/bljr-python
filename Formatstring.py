# Format string

## STRING
nama = 'Nino'
format_str = f"halo {nama}"
print(format_str)

## ANGKA
angka = 2007.5
format_str = f"angka = {angka}"
print(format_str)

## BOOLEAN
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

## Bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

## Bilangan ribuan
angka = 20000
format_str = f"ribuan = {angka:,}"
print(format_str)

## Bilangan Desimal
angka = 2007.5430
format_str = f"desimal = {angka:.3f}"
print(format_str)

## Menampilkan leading zero
angka = 2007.5430
format_str = f"desimal = {angka:02.3f}"
print(format_str)

## Menampilkan tanda + atau -
angka_min = -3
angka_plus = 10.92027
format_minus = f"minus = {angka_min:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

## memformat persen
presentase = 0.80
format_persen = f"persen= {presentase:.2%}"
print(format_persen)

## melakukan operasi aritmatika di dalam placeholder
harga_barang = 50000
jumlah = 10
format_string = f"Harga= Rp.{harga_barang*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
