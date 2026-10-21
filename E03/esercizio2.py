n = int(input("Scrivi un numero intero: "))
bit = int(input("Scrivi quanti bit vuoi utilizzare: "))
print(bin(n))
print(hex(n))
sinistra = n << bit
destra = n >> bit
print("bin sinistra", bin(sinistra))
print("esa sinistra", hex(sinistra))
print("bin destra", bin(destra))
print("esa destra", hex(destra))