import numpy as np
import matplotlib.pyplot as plt
from esercizio2 import random_walk 

N = 1000 #numero passi
s = 1 #lughezza passi
n_walker = 5 #numero walker


#liste per memorizzare le posizioni
x_walk = [] 
y_walk = []

for i in range(n_walker):
    dx, dy = random_walk(s,N)
    
    x = np.cumsum(dx)
    y = np.cumsum(dy)
    
    x_walk.append(x)
    y_walk.append(y)
    
    
plt.figure(figsize =(8, 6))

for i in range(n_walker):
    plt.plot(x_walk[i], y_walk[i],)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random walk 2D")
plt.show()

fig , ax = plt.subplots(1, 2, figsize = (13, 5))
for i in range(n_walker):
    ax[0].plot(x_walk[i], y_walk[i])
    
ax[0].set_title("Random walk 2D")
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
for i in range(n_walker):
    r_2 = x_walk[i]**2 + y_walk[i]**2
    ax[1].plot(r_2)
ax[1].set_title("Distanza quadratica")
ax[1].set_xlabel("Numero passi")
ax[1].set_ylabel("r^2")
plt.tight_layout()
plt.show()
