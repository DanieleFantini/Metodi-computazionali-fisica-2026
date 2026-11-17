
import numpy as np

def random_walk(s, N):
    """
    Genera un random walk bidimensionale.

    Parametri:
        s: lunghezza costante del passo
        N: numero di passi

    Restituisce:
        dx: array degli spostamenti lungo x
        dy: array degli spostamenti lungo y
    """
    
    phi = np.random.uniform(0, 2*np.pi, N)
    dx = s * np.cos(phi)
    dy = s * np.sin(phi)

    return dx, dy
    