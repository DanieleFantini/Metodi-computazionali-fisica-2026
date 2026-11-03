import numpy as np
import pandas as pd
import math

def somme(n):
    """
    Somma dei primi n numeeri naturali.
    """
    somma = 0
    for i in range(0, n+1):
        somma = somma + i
    return somma

def rad_somme(n):
    """
    Somma delle radici dei primi n numeri naturali.
    """
    rad_somma = 0
    for i in range(0, n+1):
        rad_somma = rad_somma + math.sqrt(i)
    return rad_somma

def s_p(n):
    """
    Somma e prodotto dei primi n numeri naturali.
    """
    somma = 0 
    prodotto = 1
    for i in range(0, n+1):
        somma = somma + i
    for i in range(1, n+1):
        prodotto = prodotto * i
    return somma, prodotto

def potenza(n, a = 1):
    """
    Calcola la somma della potenza dei primi n numeri elevati ad a.
    Se a non viene specificato, il valore di default è 1.
    """
    somma = 0 
    for i in range(0, n+1):
        somma = somma + i**a
    return somma