import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = "ExoplanetsPars_2025.csv"
df = pd.read_csv(file, comment="#")
print(df.columns)
print(df.head())
tempo = df['pl_orbper']
massa = df['pl_bmassj']
plt.scatter(np.log(tempo), np.log(massa))
plt.xlabel('periodo orbitale')
plt.ylabel('Massa')
plt.savefig("figura2.1.png")
plt.show()
plt.close()

R_max = df['pl_orbsmax']
m_star = df['st_mass']
plt.scatter(np.log(tempo), np.log(R_max**2/m_star), edgecolors = "orange")
plt.xlabel('periodo orbitale')
plt.savefig("figura2.2.png")
plt.show()
plt.close()

df_tra = df.loc[(df['discoverymethod'] == "Transit")]
df_rad = df.loc[(df['discoverymethod'] == "Radial Velocity")]

y = df_tra['pl_bmassj']
x = df_tra['pl_orbper']
y1 = df_rad['pl_bmassj']
x1 = df_rad['pl_orbper']
plt.scatter(np.log(x), np.log(y), edgecolors= "orange", alpha = 0.5)
plt.scatter(np.log(x1), np.log(y1) )
plt.savefig("figura2.3.png")
plt.show()
plt.close()

bin = np.linspace(0, np.max(m_star))
plt.hist(y, bin)
plt.hist (y1, bin)
plt.savefig("figura2.4.png")
plt.show()
plt.close()

plt.scatter(np.log10(x), np.log10(y), edgecolors= "orange", alpha = 0.5)
plt.scatter(np.log(x1), np.log10(y1))
plt.savefig("figura2.5.png")
plt.show()
plt.close()

