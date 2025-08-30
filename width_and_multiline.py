text = "kiki"

# Left alignment (default untuk string)
print(f" '{text:<10}'")

# Right alignment
print(f" '{text:>10}'")

# Center alignment
print(f" '{text:^10}'")

# Dengan karakter fill
print(f" '{text:-<10}'")
print(f" '{text:->10}'")
print(f" '{text:-^10}'")

numeric = 10
float = 10.0

# Left alignment (default untuk string)
print(f" '{numeric:<10}'")

# Right alignment
print(f" '{numeric:>10}'")

# Center alignment
print(f" '{numeric:^10}'")

# Dengan karakter fill
print(f" '{numeric:-<10}'")
print(f" '{numeric:->10}'")
print(f" '{numeric:-^10}'")

print(f" '{float:<10}'")
print(f" '{float:>10}'")

plus = 10
minus = -10

# = alignment - padding setelah tanda
print(f" '{plus:=+10}'")
print(f" '{minus:=10}'")

# Bandingkan dengan alignment lain
print(f" '{minus:>10}'") 
print(f" '{minus:<10}'")

# width dengan variabel
width = 20
text = "dynamic"
print(f" '{text:<{width}}'")

# tabel sederhana

items = [
    ("Jambu",100000,10),
    ("Mangga",30000,30)
]

print (f"{'Produk':<12} | {'Harga':<12} | {'Stok':<12}")
print("-" * 35)

for produk, harga, stok in items:
    print(f"{produk:<12} | {harga:<12} | {stok:<12}")


