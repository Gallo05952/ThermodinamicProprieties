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

# # Stampa i risultati
# print(app.get_fluido_results_in())
# print(app.get_fluido_results_out())
# mixture_in = []
# mixture_out = []
# p_in = []
# T_in = []
# m_in = []
# p_out = []
# T_out = []
# m_out = []
# h_in = []
# h_out = []

# for fluid_name, fluid_data in app.get_fluido_results_in().items():
#     components, quantities, pressure, temperature, portata = fluid_data
#     p_in.append(pressure)
#     T_in.append(temperature)
#     m_in.append(portata)
#     # Unisci i componenti e le quantità in una stringa di miscela
#     mixture_in.append("&".join(f"{comp}[{qty}]" for comp, qty in zip(components, quantities) if comp and qty))
#     print(f"{fluid_name}: {mixture_in[-1]}")

# for fluid_name, fluid_data in app.get_fluido_results_out().items():
#     components, quantities, pressure, temperature, portata = fluid_data
#     p_out.append(pressure)
#     T_out.append(temperature)
#     m_out.append(portata)
#     # Unisci i componenti e le quantità in una stringa di miscela
#     mixture_out.append("&".join(f"{comp}[{qty}]" for comp, qty in zip(components, quantities) if comp and qty))
#     print(f"{fluid_name}: {mixture_out[-1]}")

# for i, element in enumerate(m_in):
#     h_in.append(calculate_h(mixture_in[i], p_in[i], T_in[i]))

# for i, element in enumerate(m_out):
#     h_out.append(calculate_h(mixture_out[i], p_out[i], T_out[i]))

# QScambiatore=calculate_Q(h_in,m_in,h_out,m_out)
# print(QScambiatore)

# # Crea una nuova finestra root
# root_ris = tk.Tk()
# root_ris.withdraw()  # Nasconde la finestra root

# # Mostra il popup
# messagebox.showinfo("Risultato", f"QScambiatore [kW]: {QScambiatore}")

# # Chiude la finestra root quando il popup viene chiuso
# root_ris.destroy()

    