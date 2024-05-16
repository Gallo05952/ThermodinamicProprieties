from CoolProp.CoolProp import PropsSI
import tkinter as tk
from Funzioni import *

def calculate_h(fluido, p, T):
    h=PropsSI('H', 'P', p, 'T', T, fluido)
    return h

def calculate_psat(fluido, T):
    psat=PropsSI('P', 'T', T, 'Q', 0, fluido)
    return psat

def calculate_Tsat(fluido, p):
    Tsat=PropsSI('T', 'P', p, 'Q', 0, fluido)
    return Tsat

root = tk.Tk()
app = Interfaccia(root)
app.FinestraPrincipale()
root.mainloop()

# Stampa i risultati
print(app.get_fluido_results())