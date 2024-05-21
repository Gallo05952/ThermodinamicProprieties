import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from CoolProp.CoolProp import FluidsList

class Interfaccia:
        
    def __init__(self,root):
        self.root = root
        self.fluids = FluidsList()
        self.fluido_results_in = {}
        self.fluido_results_out = {}
        
    def FinestraPrincipale(self):
        self.root.title("Finestra Principale")
        self.root.geometry("300x300")

        # TITOLO
        self.titolo= tk.Label(self.root, text="Calcolo delle proprietà termodinamiche dei fluidi")
        self.titolo.grid(row=0, column=0)

        # Scambio di Calore
        self.scambio_calore = tk.Button(
            self.root,
            text="Scambio di Calore",
            command=self.FinestraScambioQ
        )
        self.scambio_calore.grid(row=1, column=0)

        # Self Condzioni di Saturazione
        self.condizioni_saturazione = tk.Button(
            self.root,
            text="Condizioni di Saturazione",
            command=self.FinestraCondizioniSaturazione
        )
        self.condizioni_saturazione.grid(row=2, column=0)

    def FinestraCondizioniSaturazione(self):
        self.FinesCondizioniSaturazione = tk.Toplevel(self.root)
        self.FinesCondizioniSaturazione.title("Finestra Condizioni di Saturazione")
        self.FinesCondizioniSaturazione.geometry("400x200")

        # TITOLO
        self.label_titolo= tk.Label(self.FinesCondizioniSaturazione, text="Calcolo delle proprietà termodinamiche dei fluidi")
        self.label_titolo.grid(row=0, column=0)

        # Scegli la proprietà
        self.Button_Tsat = tk.Button(
            self.FinesCondizioniSaturazione,
            text="Temperatura di Saturazione",
            command=self.FinestraTsat
        )
        self.Button_Tsat.grid(row=1, column=0)

        self.Button_Psat = tk.Button(
            self.FinesCondizioniSaturazione,
            text="Pressione di Saturazione",
            command=self.FinestraPsat
        )
        self.Button_Psat.grid(row=2, column=0)

        self.ButtonChiusura = tk.Button(
            self.FinesCondizioniSaturazione,
            text="Chiudi",
            command=self.FinesCondizioniSaturazione.destroy
        )
        self.ButtonChiusura.grid(row=3, column=0)

    def FinestraTsat(self):
        self.FinesTsat = tk.Toplevel(self.root)
        self.FinesTsat.title("Finestra Temperatura di Saturazione")
        self.FinesTsat.geometry("400x200")

        # TITOLO
        self.label_titolo= tk.Label(self.FinesTsat, text="Calcolo delle proprietà termodinamiche dei fluidi")
        self.label_titolo.grid(row=0, column=0)

        self.fluido_Tsat = tk.Button(
            self.FinesTsat,
            text="Fluido Tsat",
            command=lambda: self.FluidoTsat("Fluido Tsat")
        )
        self.fluido_Tsat.grid(row=1, column=0)

        #titolo inserisci pressione
        self.label_pressione = tk.Label(self.FinesTsat, text="Inserisci la pressione [barg]")
        self.label_pressione.grid(row=2, column=0)
        # Inserisci la pressione
        self.Pressione_Tsat = tk.Entry(self.FinesTsat)
        self.Pressione_Tsat.grid(row=2, column=1)

        # OK Button
        self.button_chisura_TSat = tk.Button(
            self.FinesTsat,
            text="OK",
            command=self.close_window_Tsat  # replace with the function to be executed
        )
        self.button_chisura_TSat.grid(row=3, column=0)

    def FinestraScambioQ(self):
        self.FinesScambioQ = tk.Toplevel(self.root)
        self.FinesScambioQ.title("Finestra Scambio di Calore")
        self.FinesScambioQ.geometry("500x300")
        
        # TITOLO
        self.label_titolo= tk.Label(self.FinesScambioQ, text="Calcolo delle proprietà termodinamiche dei fluidi")
        self.label_titolo.grid(row=0, column=0)

        # Fluidi input
        self.label_file_in= tk.Label(self.FinesScambioQ, text="Fluidi in input",font=("Helvetica", 12, "bold"))
        self.label_file_in.grid(row=1, column=0)
        
        # Fluido 1
        self.fluido_in1 = tk.Button(
            self.FinesScambioQ,
            text="Fluido1_IN",
            command=lambda: self.FluidoIN("Fluido1_IN")
        )
        self.fluido_in1.grid(row=2, column=0)

        # Fluido 2
        self.fluido_in2 = tk.Button(
            self.FinesScambioQ,
            text="Fluido2_IN",
            command=lambda: self.FluidoIN("Fluido2_IN")
        )
        self.fluido_in2.grid(row=3, column=0)

        # Fluido 3
        self.fluido_in3 = tk.Button(
            self.FinesScambioQ,
            text="Fluido3_IN",
            command=lambda: self.FluidoIN("Fluido3_IN")
        )
        self.fluido_in3.grid(row=4, column=0)

                # Fluidi input
        self.label_file_in= tk.Label(self.FinesScambioQ, text="Fluidi in Output",font=("Helvetica", 12, "bold"))
        self.label_file_in.grid(row=1, column=1)

        # Fluido 1 Out
        self.fluido_out1 = tk.Button(
            self.FinesScambioQ,
            text="Fluido1_OUT",
            command=lambda: self.FluidoOUT("Fluido1_OUT")
        )
        self.fluido_out1.grid(row=2, column=1)

        # Fluido 2 Out
        self.fluido_out2 = tk.Button(
            self.FinesScambioQ,
            text="Fluido2_OUT",
            command=lambda: self.FluidoOUT("Fluido2_OUT")
        )
        self.fluido_out2.grid(row=3, column=1)

        # Fluido 3 Out
        self.fluido_out3 = tk.Button(
            self.FinesScambioQ,
            text="Fluido3_OUT",
            command=lambda: self.FluidoOUT("Fluido3_OUT")
        )
        self.fluido_out3.grid(row=4, column=1)

        # OK Button
        self.ok_button_chisura = tk.Button(
            self.FinesScambioQ,
            text="OK",
            command=self.close_window  # replace with the function to be executed
)
        self.ok_button_chisura.grid(row=5, column=0, columnspan=2)

    def FluidoOUT(self, fluido_out):
        self.InserimentoFluidoOut = tk.Toplevel(self.root)
        self.InserimentoFluidoOut.title("Inserimento Fluido")
        self.InserimentoFluidoOut.geometry("500x300")

        self.LabelFluido = tk.Label(self.InserimentoFluidoOut, text="Inserisci la composizione del fluido")
        self.LabelFluido.grid(row=0, column=0)

        # Crea una StringVar per ogni Entry
        self.QuantitaFC1_out_var = tk.StringVar()
        self.QuantitaFC2_out_var = tk.StringVar()
        self.QuantitaFC3_out_var = tk.StringVar()
        self.QuantitaFC4_out_var = tk.StringVar()
        self.QuantitaFC5_out_var = tk.StringVar()

        # Crea una lista di StringVars
        self.Quantita_vars = [self.QuantitaFC1_out_var, self.QuantitaFC2_out_var, self.QuantitaFC3_out_var, self.QuantitaFC4_out_var, self.QuantitaFC5_out_var]

        # Crea una Entry per ogni StringVar
        self.QuantitaFC1_out = tk.Entry(self.InserimentoFluidoOut, textvariable=self.QuantitaFC1_out_var)
        self.QuantitaFC1_out.grid(row=1, column=1)
        
        self.QuantitaFC2_out = tk.Entry(self.InserimentoFluidoOut, textvariable=self.QuantitaFC2_out_var)
        self.QuantitaFC2_out.grid(row=2, column=1)

        self.QuantitaFC3_out = tk.Entry(self.InserimentoFluidoOut, textvariable=self.QuantitaFC3_out_var)
        self.QuantitaFC3_out.grid(row=3, column=1)

        self.QuantitaFC4_out = tk.Entry(self.InserimentoFluidoOut, textvariable=self.QuantitaFC4_out_var)
        self.QuantitaFC4_out.grid(row=4, column=1)

        self.QuantitaFC5_out = tk.Entry(self.InserimentoFluidoOut, textvariable=self.QuantitaFC5_out_var)
        self.QuantitaFC5_out.grid(row=5, column=1)

        self.FluidoC1_out=ttk.Combobox(self.InserimentoFluidoOut, values=self.fluids)
        self.FluidoC1_out.grid(row=1, column=0)

        self.FluidoC2_out=ttk.Combobox(self.InserimentoFluidoOut, values=self.fluids)
        self.FluidoC2_out.grid(row=2, column=0)

        self.FluidoC3_out=ttk.Combobox(self.InserimentoFluidoOut, values=self.fluids)
        self.FluidoC3_out.grid(row=3, column=0)

        self.FluidoC4_out=ttk.Combobox(self.InserimentoFluidoOut, values=self.fluids)
        self.FluidoC4_out.grid(row=4, column=0)

        self.FluidoC5_out=ttk.Combobox(self.InserimentoFluidoOut, values=self.fluids)
        self.FluidoC5_out.grid(row=5, column=0)

        self.Fluidopressione_out=tk.Label(self.InserimentoFluidoOut, text="Inserisci la pressione [barg]")
        self.Fluidopressione_out.grid(row=6, column=0)

        self.Pressione_out=tk.Entry(self.InserimentoFluidoOut)
        self.Pressione_out.grid(row=6, column=1)

        self.FluidoTemperatura_out=tk.Label(self.InserimentoFluidoOut, text="Inserisci la temperatura [°C]")
        self.FluidoTemperatura_out.grid(row=7, column=0)

        self.Temperatura_out=tk.Entry(self.InserimentoFluidoOut)
        self.Temperatura_out.grid(row=7, column=1)

        self.FluidoPortata_out=tk.Label(self.InserimentoFluidoOut, text="Inserisci la portata [kg/h]")
        self.FluidoPortata_out.grid(row=8, column=0)

        self.Portata_out=tk.Entry(self.InserimentoFluidoOut)
        self.Portata_out.grid(row=8, column=1)

        # Crea la label rimanenza
        self.rimanenza = tk.Label(self.InserimentoFluidoOut, text='1')
        self.rimanenza.grid(row=5, column=3)

        # Chiama aggiorna_rimanenza ogni volta che una StringVar cambia
        for quantita_var in self.Quantita_vars:
            quantita_var.trace('w', self.aggiorna_rimanenza)

        self.ok_button_out = tk.Button(self.InserimentoFluidoOut, text="OK", command=self.SalvataggioFluidoOUT)
        self.ok_button_out.grid(row=9, column=1)
        self.ok_button_out.bind('<Button-1>', lambda event: self.cambia_colore(fluido_out))
        
    def SalvataggioFluidoOUT(self):
        try:
            self.Fluido1_out=self.FluidoC1_out.get()
            self.Fluido2_out=self.FluidoC2_out.get()
            self.Fluido3_out=self.FluidoC3_out.get()
            self.Fluido4_out=self.FluidoC4_out.get()
            self.Fluido5_out=self.FluidoC5_out.get()
            self.Quantita1_out=self.QuantitaFC1_out_var.get()
            self.Quantita2_out=self.QuantitaFC2_out_var.get()
            self.Quantita3_out=self.QuantitaFC3_out_var.get()
            self.Quantita4_out=self.QuantitaFC4_out_var.get()
            self.Quantita5_out=self.QuantitaFC5_out_var.get()
            self.Pressione_out=self.Pressione_out.get()
            self.Temperatura_out=self.Temperatura_out.get()
            self.Portata_out=self.Portata_out.get()
            SpecieChimiche_out=[self.Fluido1_out, self.Fluido2_out, self.Fluido3_out, self.Fluido4_out, self.Fluido5_out]
            Quantita_out=[self.Quantita1_out, self.Quantita2_out, self.Quantita3_out, self.Quantita4_out, self.Quantita5_out]
            key = f"Fluido_{len(self.fluido_results_out) + 1}"
            self.fluido_results_out[key] = (SpecieChimiche_out, Quantita_out, self.Pressione_out, self.Temperatura_out, self.Portata_out)
        except AttributeError:
            print("Errore")
        finally:
            getattr(self.InserimentoFluidoOut, 'destroy', lambda: None)()

    def FluidoIN(self, fluido_in):
        self.InserimentoFluido = tk.Toplevel(self.root)
        self.InserimentoFluido.title("Inserimento Fluido")
        self.InserimentoFluido.geometry("500x300")

        self.LabelFluido = tk.Label(self.InserimentoFluido, text="Inserisci la composizione del fluido")
        self.LabelFluido.grid(row=0, column=0)

        # Crea una StringVar per ogni Entry
        self.QuantitaFC1_var = tk.StringVar()
        self.QuantitaFC2_var = tk.StringVar()
        self.QuantitaFC3_var = tk.StringVar()
        self.QuantitaFC4_var = tk.StringVar()
        self.QuantitaFC5_var = tk.StringVar()

        # Crea una lista di StringVars
        self.Quantita_vars = [self.QuantitaFC1_var, self.QuantitaFC2_var, self.QuantitaFC3_var, self.QuantitaFC4_var, self.QuantitaFC5_var]

        # Crea una Entry per ogni StringVar
        self.QuantitaFC1 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC1_var)
        self.QuantitaFC1.grid(row=1, column=1)

        self.QuantitaFC2 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC2_var)
        self.QuantitaFC2.grid(row=2, column=1)

        self.QuantitaFC3 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC3_var)
        self.QuantitaFC3.grid(row=3, column=1)

        self.QuantitaFC4 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC4_var)
        self.QuantitaFC4.grid(row=4, column=1)

        self.QuantitaFC5 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC5_var)
        self.QuantitaFC5.grid(row=5, column=1)

        self.FluidoC1=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC1.grid(row=1, column=0)

        self.FluidoC2=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC2.grid(row=2, column=0)

        self.FluidoC3=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC3.grid(row=3, column=0)

        self.FluidoC4=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC4.grid(row=4, column=0)

        self.FluidoC5=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC5.grid(row=5, column=0)

        self.Fluidopressione=tk.Label(self.InserimentoFluido, text="Inserisci la pressione [barg]")
        self.Fluidopressione.grid(row=6, column=0)

        self.Pressione=tk.Entry(self.InserimentoFluido)
        self.Pressione.grid(row=6, column=1)

        self.FluidoTemperatura=tk.Label(self.InserimentoFluido, text="Inserisci la temperatura [°C]")
        self.FluidoTemperatura.grid(row=7, column=0)

        self.Temperatura=tk.Entry(self.InserimentoFluido)
        self.Temperatura.grid(row=7, column=1)

        self.FluidoPortata_in=tk.Label(self.InserimentoFluido, text="Inserisci la portata [kg/h]")
        self.FluidoPortata_in.grid(row=8, column=0)

        self.Portata_in=tk.Entry(self.InserimentoFluido)
        self.Portata_in.grid(row=8, column=1)

        # Crea la label rimanenza
        self.rimanenza = tk.Label(self.InserimentoFluido, text='1')
        self.rimanenza.grid(row=5, column=3)

        # Chiama aggiorna_rimanenza ogni volta che una StringVar cambia
        for quantita_var in self.Quantita_vars:
            quantita_var.trace('w', self.aggiorna_rimanenza)

        self.ok_button = tk.Button(self.InserimentoFluido, text="OK", command=self.SalvataggioFluidoIN)
        self.ok_button.grid(row=9, column=1)
        self.ok_button.bind('<Button-1>', lambda event: self.cambia_colore(fluido_in))

    def aggiorna_rimanenza(self, *args):
        Quantita_non_vuoti = []

        for quantita_var in self.Quantita_vars:
            valore = quantita_var.get()
            if valore != '':
                Quantita_non_vuoti.append(float(valore))

        rimanenza = 1 - sum(Quantita_non_vuoti)

        self.rimanenza.config(text=rimanenza)

    def SalvataggioFluidoIN(self):
        try:
            self.Fluido1=self.FluidoC1.get()
            self.Fluido2=self.FluidoC2.get()
            self.Fluido3=self.FluidoC3.get()
            self.Fluido4=self.FluidoC4.get()
            self.Fluido5=self.FluidoC5.get()
            self.Quantita1=self.QuantitaFC1_var.get()
            self.Quantita2=self.QuantitaFC2_var.get()
            self.Quantita3=self.QuantitaFC3_var.get()
            self.Quantita4=self.QuantitaFC4_var.get()
            self.Quantita5=self.QuantitaFC5_var.get()
            self.Pressione=self.Pressione.get()
            self.Temperatura=self.Temperatura.get()
            self.Portata=self.Portata_in.get()
            SpecieChimiche=[self.Fluido1, self.Fluido2, self.Fluido3, self.Fluido4, self.Fluido5]
            Quantita=[self.Quantita1, self.Quantita2, self.Quantita3, self.Quantita4, self.Quantita5]
            key = f"Fluido_{len(self.fluido_results_in) + 1}"
            self.fluido_results_in[key] = (SpecieChimiche, Quantita, self.Pressione, self.Temperatura, self.Portata)
        except AttributeError:
            print("Errore")
        finally:
            getattr(self.InserimentoFluido, 'destroy', lambda: None)()

    def get_fluido_results_in(self):
        return self.fluido_results_in

    def get_fluido_results_out(self):
        return self.fluido_results_out

    def cambia_colore(self,fluid_in):
        if fluid_in == "Fluido1_IN":
            self.fluido_in1.config(bg='green')  # Sostituisci 'nuovo_colore' con il colore desiderato
        elif fluid_in == "Fluido2_IN":
            self.fluido_in2.config(bg='green')  # Sostituisci 'nuovo_colore' con il colore desiderato
        elif fluid_in == "Fluido3_IN":
            self.fluido_in3.config(bg='green')
        elif fluid_in == "Fluido1_OUT":
            self.fluido_out1.config(bg='green')
        elif fluid_in == "Fluido2_OUT":
            self.fluido_out2.config(bg='green')
        elif fluid_in == "Fluido3_OUT":
            self.fluido_out3.config(bg='green')
        else:
            print("Errore")

    def save_data(self):
        self.fluido_results_in = self.get_fluido_results_in()
        self.fluido_results_out = self.get_fluido_results_out()

    def FluidoTsat(self, fluido_in):
        self.InserimentoFluido = tk.Toplevel(self.root)
        self.InserimentoFluido.title("Inserimento Fluido")
        self.InserimentoFluido.geometry("500x300")

        self.LabelFluido = tk.Label(self.InserimentoFluido, text="Inserisci la composizione del fluido")
        self.LabelFluido.grid(row=0, column=0)

        # Crea una StringVar per ogni Entry
        self.QuantitaFC1_var = tk.StringVar()
        self.QuantitaFC2_var = tk.StringVar()
        self.QuantitaFC3_var = tk.StringVar()
        self.QuantitaFC4_var = tk.StringVar()
        self.QuantitaFC5_var = tk.StringVar()

        # Crea una lista di StringVars
        self.Quantita_vars = [self.QuantitaFC1_var, self.QuantitaFC2_var, self.QuantitaFC3_var, self.QuantitaFC4_var, self.QuantitaFC5_var]

        # Crea una Entry per ogni StringVar
        self.QuantitaFC1 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC1_var)
        self.QuantitaFC1.grid(row=1, column=1)

        self.QuantitaFC2 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC2_var)
        self.QuantitaFC2.grid(row=2, column=1)

        self.QuantitaFC3 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC3_var)
        self.QuantitaFC3.grid(row=3, column=1)

        self.QuantitaFC4 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC4_var)
        self.QuantitaFC4.grid(row=4, column=1)

        self.QuantitaFC5 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC5_var)
        self.QuantitaFC5.grid(row=5, column=1)

        self.FluidoC1=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC1.grid(row=1, column=0)

        self.FluidoC2=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC2.grid(row=2, column=0)

        self.FluidoC3=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC3.grid(row=3, column=0)

        self.FluidoC4=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC4.grid(row=4, column=0)

        self.FluidoC5=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC5.grid(row=5, column=0)

        self.rimanenza = tk.Label(self.InserimentoFluido, text='1')
        self.rimanenza.grid(row=5, column=3)

        # Chiama aggiorna_rimanenza ogni volta che una StringVar cambia
        for quantita_var in self.Quantita_vars:
            quantita_var.trace('w', self.aggiorna_rimanenza)

        self.ok_button = tk.Button(self.InserimentoFluido, text="OK", command=self.SalvataggioFluidoTSat)
        self.ok_button.grid(row=9, column=1)
        self.ok_button.bind('<Button-1>', lambda event: self.cambia_colore(fluido_in))

    def FluidoPsat(self, fluido_in):
        self.InserimentoFluido = tk.Toplevel(self.root)
        self.InserimentoFluido.title("Inserimento Fluido")
        self.InserimentoFluido.geometry("500x300")

        self.LabelFluido = tk.Label(self.InserimentoFluido, text="Inserisci la composizione del fluido")
        self.LabelFluido.grid(row=0, column=0)

        # Crea una StringVar per ogni Entry
        self.QuantitaFC1_var = tk.StringVar()
        self.QuantitaFC2_var = tk.StringVar()
        self.QuantitaFC3_var = tk.StringVar()
        self.QuantitaFC4_var = tk.StringVar()
        self.QuantitaFC5_var = tk.StringVar()

        # Crea una lista di StringVars
        self.Quantita_vars = [self.QuantitaFC1_var, self.QuantitaFC2_var, self.QuantitaFC3_var, self.QuantitaFC4_var, self.QuantitaFC5_var]

        # Crea una Entry per ogni StringVar
        self.QuantitaFC1 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC1_var)
        self.QuantitaFC1.grid(row=1, column=1)

        self.QuantitaFC2 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC2_var)
        self.QuantitaFC2.grid(row=2, column=1)

        self.QuantitaFC3 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC3_var)
        self.QuantitaFC3.grid(row=3, column=1)

        self.QuantitaFC4 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC4_var)
        self.QuantitaFC4.grid(row=4, column=1)

        self.QuantitaFC5 = tk.Entry(self.InserimentoFluido, textvariable=self.QuantitaFC5_var)
        self.QuantitaFC5.grid(row=5, column=1)

        self.FluidoC1=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC1.grid(row=1, column=0)

        self.FluidoC2=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC2.grid(row=2, column=0)

        self.FluidoC3=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC3.grid(row=3, column=0)

        self.FluidoC4=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC4.grid(row=4, column=0)

        self.FluidoC5=ttk.Combobox(self.InserimentoFluido, values=self.fluids)
        self.FluidoC5.grid(row=5, column=0)

        self.rimanenza = tk.Label(self.InserimentoFluido, text='1')
        self.rimanenza.grid(row=5, column=3)

        # Chiama aggiorna_rimanenza ogni volta che una StringVar cambia
        for quantita_var in self.Quantita_vars:
            quantita_var.trace('w', self.aggiorna_rimanenza)

        self.ok_button = tk.Button(self.InserimentoFluido, text="OK", command=self.SalvataggioFluidopSat)
        self.ok_button.grid(row=9, column=1)

    def SalvataggioFluidoTSat(self):
        self.Fluido1=self.FluidoC1.get()
        self.Fluido2=self.FluidoC2.get()
        self.Fluido3=self.FluidoC3.get()
        self.Fluido4=self.FluidoC4.get()
        self.Fluido5=self.FluidoC5.get()
        self.Quantita1=self.QuantitaFC1_var.get()
        self.Quantita2=self.QuantitaFC2_var.get()
        self.Quantita3=self.QuantitaFC3_var.get()
        self.Quantita4=self.QuantitaFC4_var.get()
        self.Quantita5=self.QuantitaFC5_var.get()
        SpecieChimiche=[self.Fluido1, self.Fluido2, self.Fluido3, self.Fluido4, self.Fluido5]
        Quantita=[self.Quantita1, self.Quantita2, self.Quantita3, self.Quantita4, self.Quantita5]
        key = f"Fluido_{len(self.fluido_results_in) + 1}"
        self.fluido_results_in[key] = (SpecieChimiche, Quantita)
            # Unisci i componenti e le quantità in una stringa di miscela
        self.mixtureTsat='&'.join([f"{comp}[{qty}]" for comp, qty in zip(SpecieChimiche, Quantita) if comp and qty])
        print(f"{key}: {self.mixtureTsat}")
        getattr(self.InserimentoFluido, 'destroy', lambda: None)()

    def close_window_Tsat(self):
        fluido=self.mixtureTsat
        p=self.Pressione_Tsat.get()
        try:
            Tsat=self.calculate_Tsat(fluido, p)
            messagebox.showinfo("Risultato", f"Temperatura di Saturazione [°C]: {Tsat}")
        except ValueError:
            messagebox.showinfo("Errore", "Condizioni non coperte dal databse")
        finally:
            self.FinesCondizioniSaturazione.destroy()

    def calculate_Tsat(self,fluido, p):
        from CoolProp.CoolProp import PropsSI
        p=(float(p)+1)*1e5
        Tsat=PropsSI('T', 'P', p, 'Q', 0, fluido)
        return Tsat-273.15

    def FinestraPsat(self):
        self.FinesPsat = tk.Toplevel(self.root)
        self.FinesPsat.title("Finestra Pressione di Saturazione")
        self.FinesPsat.geometry("400x200")

        # TITOLO
        self.label_titolo= tk.Label(self.FinesPsat, text="Calcolo delle proprietà termodinamiche dei fluidi")
        self.label_titolo.grid(row=0, column=0)

        self.fluido_Psat = tk.Button(
            self.FinesPsat,
            text="Fluido Psat",
            command=lambda: self.FluidoPsat("Fluido Psat")
        )
        self.fluido_Psat.grid(row=1, column=0)

        #titolo inserisci pressione
        self.label_temperatura = tk.Label(self.FinesPsat, text="Inserisci la temperatura [°C]")
        self.label_temperatura.grid(row=2, column=0)
        # Inserisci la pressione
        self.Temperatura_Psat = tk.Entry(self.FinesPsat)
        self.Temperatura_Psat.grid(row=2, column=1)

        # OK Button
        self.button_chisura_PSat = tk.Button(
            self.FinesPsat,
            text="OK",
            command=self.close_window_Psat  # replace with the function to be executed
        )
        self.button_chisura_PSat.grid(row=3, column=0)

    

    def SalvataggioFluidopSat(self):
        self.Fluido1=self.FluidoC1.get()
        self.Fluido2=self.FluidoC2.get()
        self.Fluido3=self.FluidoC3.get()
        self.Fluido4=self.FluidoC4.get()
        self.Fluido5=self.FluidoC5.get()
        self.Quantita1=self.QuantitaFC1_var.get()
        self.Quantita2=self.QuantitaFC2_var.get()
        self.Quantita3=self.QuantitaFC3_var.get()
        self.Quantita4=self.QuantitaFC4_var.get()
        self.Quantita5=self.QuantitaFC5_var.get()
        SpecieChimiche=[self.Fluido1, self.Fluido2, self.Fluido3, self.Fluido4, self.Fluido5]
        Quantita=[self.Quantita1, self.Quantita2, self.Quantita3, self.Quantita4, self.Quantita5]
        key = f"Fluido_{len(self.fluido_results_in) + 1}"
        self.fluido_results_in[key] = (SpecieChimiche, Quantita)
            # Unisci i componenti e le quantità in una stringa di miscela
        self.mixturePsat='&'.join([f"{comp}[{qty}]" for comp, qty in zip(SpecieChimiche, Quantita) if comp and qty])
        print(f"{key}: {self.mixturePsat}")
        getattr(self.InserimentoFluido, 'destroy', lambda: None)()

    def close_window_Psat(self):
        fluido=self.mixturePsat
        T=self.Temperatura_Psat.get()
        try:
            Psat=self.calculate_Psat(fluido, T)
            messagebox.showinfo("Risultato", f"Pressione di Saturazione [barg]: {Psat}")
        except ValueError:
            messagebox.showinfo("Errore", "Condizioni non coperte dal databse")
        finally:
            self.FinesCondizioniSaturazione.destroy()

    def calculate_Psat(self,fluido, T):
        from CoolProp.CoolProp import PropsSI
        T=float(T)+273.15
        Psat=PropsSI('P', 'T', T, 'Q', 0, fluido)*1e-5
        return Psat

    def close_window(self):
        self.save_data()
        self.root.destroy()