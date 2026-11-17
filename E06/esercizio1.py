import numpy as np
import matplotlib.pyplot as plt
from matplotlib import  transforms

#HIT OR MISS
def funzione_prob(z):
    return (3/1000)*(z**2)
nsample = 10000
f_max = funzione_prob(10) 
xhm = np.random.uniform(low = 0, high = 10, size = nsample)
y = np.random.uniform(low = 0, high = f_max, size = nsample)
mask = y <= funzione_prob(xhm)
valori_giusti = xhm[mask]


plt.figure(figsize=(10, 6))

plt.hist(valori_giusti, bins=100, density = True, alpha=0.5, label="Hit or Miss")
plt.xlabel('Hit or Miss Selected X')
plt.ylabel('Hit or Miss Selected Y')
plt.show()
#CUMULATIVA
def cumulativa(z):
    """
    x = C^-1(z)
    """
    return 10 * z**(1/3)


x1 = np.random.uniform(low = 0, high = 1, size = nsample)
y1 = cumulativa(x1)
plt.figure(figsize=(10, 6))

plt.hist(y1, bins=100, density=True, alpha=0.5,label="cumulative")
plt.xlabel('cumulative Selected X')
plt.ylabel('cumulative Selected Y')
plt.show()