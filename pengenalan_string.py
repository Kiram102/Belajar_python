# 1. Cara membuat string

'''
    1. Dengan single quote '...'
    2. Dengan double quote "..."
'''

data = 'ini menggunakan single quote'
print(data)
data = "ini menggunakan double quote"
print(data)

print('"Halo apa kabar?"')
print("'Halo apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at') 
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\kiki")

# tab
print("Ucup\totong, lagi jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("Baris pertama, \nBaris kedua") # LF -> line feed
print("Baris pertama, \rBaris kedua") # CR -> carriage return
print("Baris pertama, \r\nBaris kedua") # CRLF -> line feed carriage return

# 3. String literal atau raw
print('C:\new folder') # akan salah pathnya

#menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
        Nama: Kiki
        Kelas: XII RPL1
      """)

# multiline litral dan raw
print(r"""
Nama: Kiki
Kelas: XII RPL1
Website: www.kiki.com/id
      """)
