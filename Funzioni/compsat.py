from CoolProp.CoolProp import PropsSI
from CoolProp.CoolProp import FluidsList
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import numpy as np
from tkinter import filedialog

class ComposizioneSaturazione:

    def __init__(self,root):
        self.CompSat = tk.Toplevel(root)
        self.fluids = FluidsList()
        self.OperazioniIniziali()

    def Calcola(self):
        #! DA MODIFICARE SE VOGLIO UNA PRECIOSIONE MAGGIORE PER LA TEMPERATURA
        dT=0.5
        Parametri=self.ImportPreferenze()
        #TROVA LA POSIZIONE IN CUI C'è true IN fcomp
        PosizioneComp=Parametri[4].index(True)
        Intervalli=[Parametri[0], Parametri[1], Parametri[2], Parametri[3]]
        Fluidi=[self.F1, self.F2, self.F3, self.F4]
        T=Parametri[5]
        p=(float(Parametri[6])+1)*1e5
        # escludi il fluido che è stato selezionato per il completamento
        Intervalli.pop(PosizioneComp)
        Fluido_completamento=Fluidi[PosizioneComp]
        Fluidi.pop(PosizioneComp)
        MixturePossibili=[]
        #rimuovi i Booleani da Intervalli
        length=len(Intervalli)
        for i in range(len(Intervalli)):
            if Intervalli[i-1] is False:
                Intervalli.pop(i-1)
        for i in range(len(Intervalli[0])):
            if len(Intervalli)>1:
                for j in range(len(Intervalli[1])):
                    if len(Intervalli)>2:
                        for k in range(len(Intervalli[2])): 
                            Mixture = '&'.join([
                            f"{Fluidi[0]}[{Intervalli[0][i]}]",
                            f"{Fluidi[1]}[{Intervalli[1][j]}]",
                            f"{Fluidi[2]}[{Intervalli[2][k]}]",
                            f"{Fluido_completamento}[{1-Intervalli[0][i]-Intervalli[1][j]-Intervalli[2][k]}]"
                            ])
                            TSat=self.calculate_Tsat(Mixture, p)
                            if TSat is not None:
                                if abs(TSat-float(T))<dT:
                                    MixturePossibili.append(Mixture)
                    else:
                        Mixture = '&'.join([
                        f"{Fluidi[0]}[{Intervalli[0][i]}]",
                        f"{Fluidi[1]}[{Intervalli[1][j]}]",
                        f"{Fluido_completamento}[{1-Intervalli[0][i]-Intervalli[1][j]}]"
                        ])
                        TSat=self.calculate_Tsat(Mixture, p)
                        if TSat is not None:
                            if abs(TSat-float(T))<dT:
                                MixturePossibili.append(Mixture)
            else:
                Mixture = '&'.join([
                f"{Fluidi[0]}[{Intervalli[0][i]}]",
                f"{Fluido_completamento}[{1-Intervalli[0][i]}]"
                ])
                TSat=self.calculate_Tsat(Mixture, p)
                if TSat is not None:
                    if abs(TSat-float(T))<dT:
                        MixturePossibili.append(Mixture)
        #messagebox con le possibili miscele
        messagebox.showinfo("Mixture", MixturePossibili)
        print(MixturePossibili)

                                    
   

        #print(Parametri)

    def ImportPreferenze(self):
        # self.CompSat.update_idletasks()  # Aggiunge questa linea
        self.check_vars = [self.Comp1_var, self.Comp2_var, self.Comp3_var, self.Comp4_var]
        self.FComp=[]
        for var in self.check_vars:
            self.FComp.append(var.get())
        # se c'è più di un valore True mesgbox
        if self.FComp.count(True) > 1:
            messagebox.showinfo("Errore", "Seleziona solo un fluido per completare la composizione per differenza")
            return
        #! PARAMETRO DA MODIFICARE SE VOGLIO PIù PUNTI DI PROVA
        n_punti=50
        self.F1=self.FluidoC1.get()
        self.F2=self.FluidoC2.get()
        self.F3=self.FluidoC3.get()
        self.F4=self.FluidoC4.get()
        self.T=self.entry_T.get()
        self.p=self.entry_p.get()
        self.F1_min=self.QuantitaFC1_var_min.get()
        self.F1_max=self.QuantitaFC1_var_max.get()
        self.F2_min=self.QuantitaFC2_var_min.get()
        self.F2_max=self.QuantitaFC2_var_max.get()
        self.F3_min=self.QuantitaFC3_var_min.get()
        self.F3_max=self.QuantitaFC3_var_max.get()
        self.F4_min=self.QuantitaFC4_var_min.get()
        self.F4_max=self.QuantitaFC4_var_max.get()
        # print(self.F1, self.F2, self.F3, self.F4, self.T, self.p)
        # print(self.F1_min, self.F1_max, self.F2_min, self.F2_max, self.F3_min, self.F3_max, self.F4_min, self.F4_max)
        if self.F1_min != "" and self.F1_max != "":
            self.F1_min=float(self.F1_min)
            self.F1_max=float(self.F1_max)
            self.IntervalloF1 = np.linspace(self.F1_min, self.F1_max, num=n_punti)
        else: self.IntervalloF1 = False
        if self.F2_min != "" and self.F2_max != "":
            self.F2_min=float(self.F2_min)
            self.F2_max=float(self.F2_max)
            self.IntervalloF2 = np.linspace(self.F2_min, self.F2_max, num=n_punti)
        else: self.IntervalloF2 = False
        if self.F3_min != "" and self.F3_max != "":
            self.F3_min=float(self.F3_min)
            self.F3_max=float(self.F3_max)
            self.IntervalloF3 = np.linspace(self.F3_min, self.F3_max, num=n_punti)
        else: self.IntervalloF3 = False
        if self.F4_min != "" and self.F4_max != "":
            self.F4_min=float(self.F4_min)
            self.F4_max=float(self.F4_max)
            self.IntervalloF4 = np.linspace(self.F4_min, self.F4_max, num=n_punti)
        else: self.IntervalloF4 = False

        Par=[self.IntervalloF1, self.IntervalloF2, self.IntervalloF3, self.IntervalloF4, self.FComp, self.T, self.p]
        return Par

    def OperazioniIniziali(self):
        
        self.CompSat.title("Composizione di Saturazione")
        self.CompSat.geometry("1000x300")

        self.label_Titolo = tk.Label(self.CompSat, 
                                    text="Calcolo della composizione di saturazione: Confronto con la temperatura indicata",
                                    font=("Arial", 20),
                                    fg="orange")
        self.label_Titolo.grid(row=0, column=0, columnspan=4)

        #riga vuota
        self.label_vuota = tk.Label(self.CompSat, text=" ")
        self.label_vuota.grid(row=1, column=0)

        self.label_T = tk.Label(self.CompSat,
                                text="Temperatura [°C]",
                                font=("Helvetica", 12, "bold"))
        self.label_T.grid(row=2, column=0)
        self.entry_T = tk.Entry(self.CompSat)
        self.entry_T.grid(row=2, column=1)

        self.label_p = tk.Label(self.CompSat, 
                                text="Pressione [barg]",
                                font=("Helvetica", 12, "bold"))
        self.label_p.grid(row=3, column=0)
        self.entry_p = tk.Entry(self.CompSat)
        self.entry_p.grid(row=3, column=1)

        self.LabelFluido = tk.Label(self.CompSat,
                                    text="Inserisci i range di composizione in cui cercare su base molare [0,1]",
                                    font=("Helvetica", 12, "bold"))
        self.LabelFluido.grid(row=4, column=0, columnspan=4)

        self.completamento=tk.Label(self.CompSat,
                                    text="Usa questo fluido per il completamento",
                                    font=("Helvetica", 8, "bold"))
        self.completamento.grid(row=5, column=3)

        self.Quantità_min=tk.Label(self.CompSat,
                                text="Quantità minima",
                                font=("Helvetica", 8, "bold"))
        self.Quantità_min.grid(row=5, column=1)

        self.Quantità_max=tk.Label(self.CompSat,
                                text="Quantità massima",
                                font=("Helvetica", 8, "bold"))
        self.Quantità_max.grid(row=5, column=2)

                # Crea una StringVar per ogni Entry
        try:
            self.QuantitaFC1_var_min = tk.StringVar()
            self.QuantitaFC1_var_max = tk.StringVar()
            self.QuantitaFC2_var_min = tk.StringVar()
            self.QuantitaFC2_var_max = tk.StringVar()
            self.QuantitaFC3_var_min = tk.StringVar()
            self.QuantitaFC3_var_max = tk.StringVar()
            self.QuantitaFC4_var_min = tk.StringVar()
            self.QuantitaFC4_var_max = tk.StringVar()
        except Exception as e:
            print(e)

        # Crea una Entry per ogni StringVar
        self.QuantitaFC1_min = tk.Entry(self.CompSat,
                                        textvariable=self.QuantitaFC1_var_min)
        self.QuantitaFC1_min.grid(row=6, column=1)

        self.QuantitaFC1_max = tk.Entry(self.CompSat,
                                        textvariable=self.QuantitaFC1_var_max)
        self.QuantitaFC1_max.grid(row=6, column=2)

        self.QuantitaFC2_min = tk.Entry(self.CompSat,
                                        textvariable=self.QuantitaFC2_var_min)
        self.QuantitaFC2_min.grid(row=7, column=1)

        self.QuantitaFC2_max = tk.Entry(self.CompSat,
                                        textvariable=self.QuantitaFC2_var_max)
        self.QuantitaFC2_max.grid(row=7, column=2)

        self.QuantitaFC3_min = tk.Entry(self.CompSat,
                                        textvariable=self.QuantitaFC3_var_min)
        self.QuantitaFC3_min.grid(row=8, column=1)

        self.QuantitaFC3_max = tk.Entry(self.CompSat,
                                        textvariable=self.QuantitaFC3_var_max)
        self.QuantitaFC3_max.grid(row=8, column=2)

        self.QuantitaFC4_min = tk.Entry(self.CompSat,
                                        textvariable=self.QuantitaFC4_var_min)
        self.QuantitaFC4_min.grid(row=9, column=1)

        self.QuantitaFC4_max = tk.Entry(self.CompSat,
                                        textvariable=self.QuantitaFC4_var_max)
        self.QuantitaFC4_max.grid(row=9, column=2)

        self.FluidoC1=ttk.Combobox(self.CompSat,
                                values=self.fluids)
        self.FluidoC1.grid(row=6, column=0)

        self.FluidoC2=ttk.Combobox(self.CompSat,
                                values=self.fluids)
        self.FluidoC2.grid(row=7, column=0)

        self.FluidoC3=ttk.Combobox(self.CompSat,
                                values=self.fluids)
        self.FluidoC3.grid(row=8, column=0)

        self.FluidoC4=ttk.Combobox(self.CompSat,
                                values=self.fluids)
        self.FluidoC4.grid(row=9, column=0)

        try:
            self.Comp1_var = tk.BooleanVar()
            self.Comp2_var = tk.BooleanVar()
            self.Comp3_var = tk.BooleanVar()
            self.Comp4_var = tk.BooleanVar()
        except Exception as e:
            print(e)

        # self.Comp1=tk.Checkbutton(self.CompSat, variable=self.Comp1_var,command=lambda: print("Clicked!"))
        # self.Comp1.grid(row=3, column=3)
        
        self.Comp1 = tk.Checkbutton(self.CompSat,
                                    variable=self.Comp1_var)
        self.Comp1.grid(row=6, column=3)

        self.Comp2 = tk.Checkbutton(self.CompSat,
                                    variable=self.Comp2_var)
        self.Comp2.grid(row=7, column=3)

        self.Comp3 = tk.Checkbutton(self.CompSat,
                                    variable=self.Comp3_var)
        self.Comp3.grid(row=8, column=3)

        self.Comp4 = tk.Checkbutton(self.CompSat,
                                    variable=self.Comp4_var)
        self.Comp4.grid(row=9, column=3)

        self.bottone = tk.Button(self.CompSat,
                                text="Calcola",
                                font=("Helvetica", 12, "bold"),
                                bg="#D3D3D3",
                                command=self.Calcola)
        self.bottone.grid(row=10, column=1)

        self.chiusura = tk.Button(self.CompSat,
                                text="Chiudi",
                                font=("Helvetica", 12, "bold"),
                                bg="#D3D3D3",
                                command=self.CompSat.destroy)
        self.chiusura.grid(row=10, column=2)

    def calculate_Tsat(self,fluido, p):
        try:
            Tsat = PropsSI('T', 'P', p, 'Q', 0, fluido)
            return Tsat - 273.15
        except Exception as e:
            return None

