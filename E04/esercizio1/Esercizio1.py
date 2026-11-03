import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

file = "kplr010666592-2011240104155_slc.csv"

df = pd.read_csv(file)
print(df.head())
print(df.columns)

tempo = df['TIME']
flusso = df['PDCSAP_FLUX']
plt.plot(tempo, flusso, '.')
plt.errorbar(tempo, flusso, yerr=df['PDCSAP_FLUX_ERR'], xerr = df['TIMECORR'], fmt='.', ecolor='red')
plt.xlabel('Time')
plt.ylabel('Flux')
plt.show()

fl_min = np.nanargmin(flusso.to_numpy())
t_min = tempo.iloc[fl_min]
intorno = 0.5   
df_min = df.loc[(tempo >= t_min - intorno) & (tempo <= t_min + intorno)]
tempo_min = df_min['TIME']
flusso_min = df_min['PDCSAP_FLUX']
plt.plot(tempo_min, flusso_min, '.')
plt.errorbar(tempo_min, flusso_min, yerr=df_min['PDCSAP_FLUX_ERR'], fmt='.', ecolor='red')
plt.xlabel('Time')
plt.ylabel('Flux')
plt.show()

fig, ax = plt.subplots(figsize=(12,6))
ax_in = inset_axes(ax, width="30%", height="30%", loc='upper right')
ax.plot(tempo, flusso, '.')
ax_in.errorbar(tempo_min, flusso_min, yerr=df_min['PDCSAP_FLUX_ERR'], fmt='.', ecolor='red')
plt.show()
