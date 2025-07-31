a = 10
b = 2

#pertambahan +
hasil = a + b
print(a,"+",b,"=", hasil)

#pengurangan -
hasil = a - b
print(a,"-",b,"=", hasil)

#perkalian *
hasil = a * b
print(a,"x",b,"=", hasil)

#pembagian /
hasil = a / b
print(a,":",b,"=", hasil)

#eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=", hasil)

#modulus %
hasil = a % b
print(a,"%",b,"=", hasil)

#floor division //
hasil = a // b
print(a,"//",b,"=", hasil)

#operational precedence pokoknya yang pake () berarti angka yang akan di jalankan duluan
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=", hasil)

hasil = x + y * z
print(x,"+",y,"*",z,"=",hasil)

hasil = (x + y) * z
print("(",x,"+",y,")","*",z,"=",hasil)