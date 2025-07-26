print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukan Celcius:"))
print("Suhu adalah",celcius,"Celcius")

reamur = (4/5) * celcius
print("reamur adalah :",reamur)

fahrenmit = ((9/5) * celcius) + 32
print("fahremit adalah :",fahrenmit)

kelvin = celcius + 273
print("kelvin adalah :",kelvin)

print("=====Fahrenheit ke kelvin=====")
fahrenheit = float(input("Masukan Suhu Fahrenheit : "))
celcius    = (5/9) * (fahrenheit - 32)
kelvin     = (celcius + 273)
print("Suhu dalam Kelvin : ", kelvin)

print("=====kelvin ke fahrenheit======")
kelvin     = float(input("Masukan Suhu Dalam kelvin : "))
celcius    = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit : ", fahrenheit)