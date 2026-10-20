l1 = ['Lunedí', 'Martedí', 'Mercoledí', 'Giovedí', 'Venerdí', 'Sabato', 'Domenica']
l2 = []
for i in range(1, 32):
    l2.append(i)
lunghezza = len(l2)
d1 ={l2[i]:l1[(i+3)%7] for i in range(lunghezza)}
print(d1)


