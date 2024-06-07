from CoolProp.CoolProp import PropsSI
import tkinter as tk
from tkinter import messagebox
from Funzioni import *

def calculate_h(fluido, p, T):
    p=(float(p)+1)*10**5
    T=float(T)+273.15
    h = PropsSI('H', 'P', p, 'T', T, fluido)
    return h/1000

def calculate_psat(fluido, T):
    T=float(T)+273.15
    psat=PropsSI('P', 'T', T, 'Q', 0, fluido)
    return psat

def calculate_Tsat(fluido, p):
    p=(float(p)+1)/10
    Tsat=PropsSI('T', 'P', p, 'Q', 0, fluido)
    return Tsat

def calculate_Q(h_in,m_in,h_out,m_out):
    Q_in=0
    i=0
    for i in range(len(h_in)):
        Q_in+=h_in[i]*float(m_in[i])/3600
    Q_out=0
    j=0
    for j in range(len(h_out)):
        Q_out+=h_out[j]*float(m_out[j])/3600
    Q=Q_in-Q_out
    return Q

root = tk.Tk()
app = Interfaccia(root)
app.FinestraPrincipale()
root.mainloop()
