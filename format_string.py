# format string

#string
nama = "kiki"
format_str = f"Hello : {nama}"
print(format_str) 

#angka
age = 20.0
format_int = f"Umur : {age}"
print(format_int)

#boolean
boolean = True
format_boolean = f"Boolean : {boolean}"
print(format_boolean)

#bilangan bulat
bulat = 20
format_bulat = f"Bulat : {bulat:d}"
print(format_bulat)

#bilangan ribuan
ribuan = 30000000000
format_ribuan = f"Ribuan : {ribuan:,}"
print(format_ribuan)

#bilangan decimal
decimal = 30000.500
format_decimal = f"Decimal : {decimal:.2f}"
print(format_decimal)   

#menampilkan leading zero
leading = 30000.500
format_leading = f"Leading : {leading:10.2f}"
print(format_leading)

#tanda plus minus
plus = 10
minus = -10
format_plus = f"Plus : {plus:+d}"
format_minus = f"Minus : {minus:+d}"
print(format_plus)
print(format_minus)

#melakukan aritmatika di placeholder
angka1 = 10000000
angka2 = 9
format_aritmatika = f"Aritmatika {angka1 * angka2}"
print(format_aritmatika)