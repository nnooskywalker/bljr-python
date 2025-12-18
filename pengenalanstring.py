data = "ini adalah string"
print(data)
print(type(data))

#1. cara membuat string

'''
    1. dengan menggunakan single quote '....''
    2. dengan menggunakan double quote "...."'
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo apa kabar ?"')
print("'Halo, apa kabar ?'")
print("ini adalah hari jum'at")

#2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash (\\)
print("C:\\user\\Ucup")

# tab (\t)
print("ucup\t\totong, semakin jauh")

# backspace (\b)
print("ucup \botong, jadi deketan")

#newline (\n)
print("baris pertama.\nbaris kedua.") #LF -> Line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") #CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") #CRLF -> Line feed carriage return -> dipakai oleh windows

#3. String Literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string and raw
print(r"""
Nama : Ucup
Kelas : 3/SD
Website : www.ucup.com/newID
""")


