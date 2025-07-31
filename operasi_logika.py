# operasi logika dan boolean

# not, or, and, xor 

# not
print("====Not====")
a = False
c = not a
print('Data a =', a)
print('---------- Not')
print('Data c =', c)

# or (jika salah satu true maka hasilnya true)
print("====Or====")
a = False
b = False
c = a or b
print(a,'Or',b,'=',c)

a = False
b = True
c = a or b
print(a,'Or',b,'=',c)

a = True
b = False
c = a or b
print(a,'Or',b,'=',c)

a = True
b = True
c = a or b
print(a,'Or',b,'=',c)


# AND (kalau and akan true jika keduanya true)
print("====And====")
a = False
b = False
c = a and b
print(a,'and',b,'=',c)

a = False
b = True
c = a and b
print(a,'and',b,'=',c)

a = True
b = False
c = a and b
print(a,'and',b,'=',c)

a = True
b = True
c = a and b
print(a,'and',b,'=',c)


# XOR (akan true jika salah satu true jika ada yang true true makan akan false)
print("====XOR====")
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)