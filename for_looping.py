# Loop 0 sampai 4
for i in range(5) :
    print(f"List i -> {i}")
print("Loop 0 sampai 4")

# Loop 1 sampai 5
for i in range(1,6) :
    print(f"List i -> {i}") 
print("Loop 1 sampai 5")

# Loop dengan langkah
for i in range(0,10,3) :
    print(f"List -> {i}")
print("Loop dengan langkah")

# Loop dengan list
list = ["Apel", "Semangka", "Mangga"]
for i in list :
    print(f"List Buah -> {i}")
print("Loop dengan list")

# Loop dengan index 
list = ["Apel", "Semangka", "Mangga"]
for index, i in enumerate(list) :
    print(f"List {index}: {i}")
print("Loop dengan index")
