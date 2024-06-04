import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from CoolProp.CoolProp import FluidsList
from .autocomplete import AutocompleteCombobox

class Interfaccia:
        
    def __init__(self,root):
        self.root = root
        self.fluids = FluidsList()
        self.fluido_results_in = {}
        self.fluido_results_out = {}
        
    def FinestraPrincipale(self):
        self.root.title("Finestra Principale")
        self.root.geometry("350x200")

        # TITOLO
        self.titolo= tk.Label(self.root,
                            text="Possibili Calcoli: Selezionare un'opzione",
                            font=("Helvetica", 12, "bold"),
                            fg="blue")
        self.titolo.grid(row=0, column=0, columnspan=2)

        # Empty row
        empty_label = tk.Label(self.root, text="")
        empty_label.grid(row=1, column=0)

        # Scambio di Calore
        self.scambio_calore = tk.Button(
            self.root,
            text="Scambio di Calore",
            font=("Helvetica", 10, "bold"),
            bg="#D3D3D3",
            command=self.FinestraScambioQ
        )
        self.scambio_calore.grid(row=2, column=0)

                # Empty row
        empty_label2 = tk.Label(self.root, text="")
        empty_label2.grid(row=3, column=0)

        # Self Condzioni di Saturazione
        self.condizioni_saturazione = tk.Button(
            self.root,
            text="Condizioni di Saturazione",
            font=("Helvetica", 10, "bold"),
            bg="#D3D3D3",
            command=self.FinestraCondizioniSaturazione
        )
        self.condizioni_saturazione.grid(row=4, column=0)

    def FinestraCondizioniSaturazione(self):

        from Funzioni.compsat import ComposizioneSaturazione

        self.FinesCondizioniSaturazione = tk.Toplevel(self.root)
        self.FinesCondizioniSaturazione.title("Finestra Condizioni di Saturazione")
        self.FinesCondizioniSaturazione.geometry("400x250")

        # TITOLO
        self.label_titolo= tk.Label(self.FinesCondizioniSaturazione, 
                                    text="Calcolo delle proprietà termodinamiche dei fluidi",
                                    font=("Helvetica", 12, "bold"),
                                    fg='green')
        self.label_titolo.grid(row=0, column=0,columnspan=2)

        self.riga_vuota = tk.Label(self.FinesCondizioniSaturazione,
                                    text="")
        self.riga_vuota.grid(row=1, column=0)

        # Scegli la proprietà
        self.Button_Tsat = tk.Button(
            self.FinesCondizioniSaturazione,
            text="Temperatura di Saturazione",
            font=("Helvetica", 10, "bold"),
            bg="#D3D3D3",
            command=self.FinestraTsat
        )
        self.Button_Tsat.grid(row=2, column=0)

        self.riga_vuota = tk.Label(self.FinesCondizioniSaturazione,
                                    text="")
        self.riga_vuota.grid(row=3, column=0)

        self.Button_Psat = tk.Button(
            self.FinesCondizioniSaturazione,
            text="Pressione di Saturazione",
            bg="#D3D3D3",
            font=("Helvetica", 10, "bold"),
            command=self.FinestraPsat
        )
        self.Button_Psat.grid(row=4, column=0)

        self.riga_vuota = tk.Label(self.FinesCondizioniSaturazione,
                                    text="")
        self.riga_vuota.grid(row=5, column=0)

        self.ComposizioneSat = tk.Button(
            self.FinesCondizioniSaturazione,
            text="Composizione di Saturazione",
            bg="#D3D3D3",
            font=("Helvetica", 10, "bold"),
            command=lambda: ComposizioneSaturazione(self.root).OperazioniIniziali())
        self.ComposizioneSat.grid(row=6, column=0)

        self.riga_vuota = tk.Label(self.FinesCondizioniSaturazione,
                                    text="")
        self.riga_vuota.grid(row=7, column=0)

        self.ButtonChiusura = tk.Button(
            self.FinesCondizioniSaturazione,
            text="Chiudi",
            bg="#D3D3D3",
            font=("Helvetica", 10, "bold"),
            command=self.FinesCondizioniSaturazione.destroy
        )
        self.ButtonChiusura.grid(row=8, column=0)

    def FinestraTsat(self):
        self.FinesTsat = tk.Toplevel(self.root)
        self.FinesTsat.title("Finestra Temperatura di Saturazione")
        self.FinesTsat.geometry("450x270")

        # TITOLO
        self.label_titolo= tk.Label(self.FinesTsat, 
                                    text="Temperatura di saturazione di una miscela di fluidi",
                                    font=("Helvetica", 12, "bold"),fg="red")
        self.label_titolo.grid(row=0, column=0, columnspan=2)

        #riga vuota
        self.riga_vuota = tk.Label(self.FinesTsat,
                                    text="")
        self.riga_vuota.grid(row=1, column=0)

        #titolo inserisci pressione
        self.label_pressione = tk.Label(self.FinesTsat, 
                                        text="Inserisci la pressione [barg]",
                                        font=("Helvetica", 12, "bold"))
        self.label_pressione.grid(row=2, column=0)
        # Inserisci la pressione
        self.Pressione_Tsat = tk.Entry(self.FinesTsat)
        self.Pressione_Tsat.grid(row=2, column=1)

        self.LabelFluido = tk.Label(self.FinesTsat,
                                    text="Inserisci la composizione del fluido: base molare",
                                    font=("Helvetica", 12, "bold"))
        self.LabelFluido.grid(row=3, column=0, columnspan=2)

        # Crea una StringVar per ogni Entry
        try:
            self.QuantitaFC1_var = tk.StringVar()
            self.QuantitaFC2_var = tk.StringVar()
            self.QuantitaFC3_var = tk.StringVar()
            self.QuantitaFC4_var = tk.StringVar()
            self.QuantitaFC5_var = tk.StringVar()
        except AttributeError:
            print("Errore")

        # Crea una lista di StringVars
        self.Quantita_vars = [self.QuantitaFC1_var, 
                            self.QuantitaFC2_var,
                            self.QuantitaFC3_var,
                            self.QuantitaFC4_var,
                            self.QuantitaFC5_var]

        # Crea una Entry per ogni StringVar
        self.QuantitaFC1 = tk.Entry(self.FinesTsat,
                                    textvariable=self.QuantitaFC1_var)
        self.QuantitaFC1.grid(row=4, column=1)

        self.QuantitaFC2 = tk.Entry(self.FinesTsat,
                                    textvariable=self.QuantitaFC2_var)
        self.QuantitaFC2.grid(row=5, column=1)

        self.QuantitaFC3 = tk.Entry(self.FinesTsat,
                                    textvariable=self.QuantitaFC3_var)
        self.QuantitaFC3.grid(row=6, column=1)

        self.QuantitaFC4 = tk.Entry(self.FinesTsat,
                                    textvariable=self.QuantitaFC4_var)
        self.QuantitaFC4.grid(row=7, column=1)

        self.QuantitaFC5 = tk.Entry(self.FinesTsat,
                                    textvariable=self.QuantitaFC5_var)
        self.QuantitaFC5.grid(row=8, column=1)

        self.FluidoC1=ttk.Combobox(self.FinesTsat,
                                values=self.fluids)
        self.FluidoC1.grid(row=4, column=0)

        self.FluidoC2=ttk.Combobox(self.FinesTsat,
                                values=self.fluids)
        self.FluidoC2.grid(row=5, column=0)

        self.FluidoC3=ttk.Combobox(self.FinesTsat,
                                    values=self.fluids)
        self.FluidoC3.grid(row=6, column=0)

        self.FluidoC4=ttk.Combobox(self.FinesTsat, 
                                values=self.fluids)
        self.FluidoC4.grid(row=7, column=0)

        self.FluidoC5=ttk.Combobox(self.FinesTsat,
                                    values=self.fluids)
        self.FluidoC5.grid(row=8, column=0)

        self.rimanenza = tk.Label(self.FinesTsat, text='1')
        self.rimanenza.grid(row=8, column=3)

        # Chiama aggiorna_rimanenza ogni volta che una StringVar cambia
        for quantita_var in self.Quantita_vars:
            quantita_var.trace('w', self.aggiorna_rimanenza)

        self.ok_button = tk.Button(self.FinesTsat,
                                text="OK",
                                font=("Helvetica", 10, "bold"),
                                bg="#D3D3D3",
                                command=self.SalvataggioFluidoTSat)
        self.ok_button.grid(row=9, column=0)

        self.closeButton = tk.Button(self.FinesTsat,
                                    text="Chiudi",
                                    font=("Helvetica", 10, "bold"),
                                    bg="#D3D3D3",
                                    command=lambda: self.distruggi(self.FinesTsat))
        self.closeButton.grid(row=9, column=1)

    def FinestraScambioQ(self):
        self.FinesScambioQ = tk.Toplevel(self.root)
        self.FinesScambioQ.title("Finestra Scambio di Calore")
        self.FinesScambioQ.geometry("500x500")
        
        # TITOLO
        self.label_titolo= tk.Label(self.FinesScambioQ,
                                    text="Calcolo delle scambio termico",
                                    font=("Helvetica", 12, "bold"),fg="red")
        self.label_titolo.grid(row=0, column=1, columnspan=3)

        #riga vuota
        self.riga_vuota = tk.Label(self.FinesScambioQ,
                                    text="")
        self.riga_vuota.grid(row=1, column=0)

        # Fluidi input
        self.label_file_in= tk.Label(self.FinesScambioQ, 
                                    text="Fluidi in input",
                                    font=("Helvetica", 10, "bold"))
        self.label_file_in.grid(row=2, column=2 )
        
        # Fluido 1
        self.fluido_in1 = tk.Button(
            self.FinesScambioQ,
            text="Fluido1_IN",
            bg="#D3D3D3",
            command=lambda: self.FluidoIN("Fluido1_IN")
        )
        self.fluido_in1.grid(row=3, column=1)

        # fluido risultante
        self.mixture_in1_var=tk.StringVar()
        self.fluido_in1_name=tk.Label(self.FinesScambioQ, 
                                    textvariable=self.mixture_in1_var)
        self.fluido_in1_name.grid(row=4, column=1)

        self.T_Label=tk.Label(self.FinesScambioQ,
                            text="Temperatura [°C]")
        self.T_Label.grid(row=5, column=0)

        self.T1_in_Entry=tk.Entry(self.FinesScambioQ)
        self.T1_in_Entry.grid(row=5, column=1)

        self.P_Label=tk.Label(self.FinesScambioQ,
                            text="Pressione [barg]")
        self.P_Label.grid(row=6, column=0)

        self.P1_in_Entry=tk.Entry(self.FinesScambioQ)
        self.P1_in_Entry.grid(row=6, column=1)
        
        self.portata=tk.Label(self.FinesScambioQ, text="Portata [kg/h]")
        self.portata.grid(row=7, column=0)

        self.portata1=tk.Entry(self.FinesScambioQ)
        self.portata1.grid(row=7, column=1)

        #empty row
        empty_label2 = tk.Label(self.FinesScambioQ, text="")
        empty_label2.grid(row=8, column=0)

        # Fluidi output
        self.label_file_in= tk.Label(self.FinesScambioQ,
                                    text="Fluidi in Output",
                                    font=("Helvetica", 10, "bold"))
        self.label_file_in.grid(row=9, column=2)


        # Fluido 1 Out
        self.fluido_out1 = tk.Button(
            self.FinesScambioQ,
            text="Fluido1_OUT",
            bg="#D3D3D3",
            command=lambda: self.FluidoOUT("Fluido1_OUT")
        )
        self.fluido_out1.grid(row=10, column=1)

        # fluido risultante
        self.mixture_out1_var = tk.StringVar()
        self.fluido_out1_name=tk.Label(self.FinesScambioQ,
                                    textvariable=self.mixture_out1_var)
        self.fluido_out1_name.grid(row=11, column=1)

        self.T_Label=tk.Label(self.FinesScambioQ,
                            text="Temperatura [°C]")
        self.T_Label.grid(row=12, column=0)

        self.T1_out_Entry=tk.Entry(self.FinesScambioQ)
        self.T1_out_Entry.grid(row=12, column=1)

        self.P_Label=tk.Label(self.FinesScambioQ,
                            text="Pressione [barg]")
        self.P_Label.grid(row=13, column=0)

        self.P1_out_Entry=tk.Entry(self.FinesScambioQ)
        self.P1_out_Entry.grid(row=13, column=1)

        self.portata=tk.Label(self.FinesScambioQ, text="Portata [kg/h]")
        self.portata.grid(row=14, column=0)

        self.portata1_out=tk.Entry(self.FinesScambioQ)
        self.portata1_out.grid(row=14, column=1)

        # Fluido 2
        self.fluido_in2 = tk.Button(
            self.FinesScambioQ,
            text="Fluido2_IN",
            bg="#D3D3D3",
            command=lambda: self.FluidoIN("Fluido2_IN")
        )
        self.fluido_in2.grid(row=3, column=2)

        #fluido risultante
        self.mixture_in2_var=tk.StringVar()
        self.fluido_in2_name=tk.Label(self.FinesScambioQ,
                                    textvariable=self.mixture_in2_var)
        self.fluido_in2_name.grid(row=4, column=2)

        self.T2_in_Entry=tk.Entry(self.FinesScambioQ)
        self.T2_in_Entry.grid(row=5, column=2)

        self.P2_in_Entry=tk.Entry(self.FinesScambioQ)
        self.P2_in_Entry.grid(row=6, column=2)

        self.portata2=tk.Entry(self.FinesScambioQ)
        self.portata2.grid(row=7, column=2)

        # Fluido 2 Out
        self.fluido_out2 = tk.Button(
            self.FinesScambioQ,
            text="Fluido2_OUT",
            bg="#D3D3D3",
            command=lambda: self.FluidoOUT("Fluido2_OUT")
        )
        self.fluido_out2.grid(row=10, column=2)

        #fluido risultante
        self.mixture_out2_var=tk.StringVar()
        self.fluido_out2_name=tk.Label(self.FinesScambioQ,
                                    textvariable=self.mixture_out2_var)
        self.fluido_out2_name.grid(row=11, column=2)

        self.T2_out_Entry=tk.Entry(self.FinesScambioQ)
        self.T2_out_Entry.grid(row=12, column=2)

        self.P2_out_Entry=tk.Entry(self.FinesScambioQ)
        self.P2_out_Entry.grid(row=13, column=2)

        self.portata2_out=tk.Entry(self.FinesScambioQ)
        self.portata2_out.grid(row=14, column=2)

        #fluido 3
        self.fluido_in3 = tk.Button(
            self.FinesScambioQ,
            text="Fluido3_IN",
            bg="#D3D3D3",
            command=lambda: self.FluidoIN("Fluido3_IN")
        )
        self.fluido_in3.grid(row=3, column=3)

        #fluido risultante
        self.mixture_in3_var=tk.StringVar()
        self.fluido_in3_name=tk.Label(self.FinesScambioQ,
                                    textvariable=self.mixture_in3_var)
        self.fluido_in3_name.grid(row=4, column=3)

        self.T3_in_Entry=tk.Entry(self.FinesScambioQ)
        self.T3_in_Entry.grid(row=5, column=3)

        self.P3_in_Entry=tk.Entry(self.FinesScambioQ)
        self.P3_in_Entry.grid(row=6, column=3)

        self.portata3=tk.Entry(self.FinesScambioQ)
        self.portata3.grid(row=7, column=3)

        #fluido 3 out
        self.fluido_out3 = tk.Button(
            self.FinesScambioQ,
            text="Fluido3_OUT",
            bg="#D3D3D3",
            command=lambda: self.FluidoOUT("Fluido3_OUT")
        )
        self.fluido_out3.grid(row=10, column=3)

        #fluido risultante
        self.mixture_out3_var=tk.StringVar()
        self.fluido_out3_name=tk.Label(self.FinesScambioQ,
                                    textvariable=self.mixture_out3_var)
        self.fluido_out3_name.grid(row=11, column=3)

        self.T3_out_Entry=tk.Entry(self.FinesScambioQ)
        self.T3_out_Entry.grid(row=12, column=3)

        self.P3_out_Entry=tk.Entry(self.FinesScambioQ)
        self.P3_out_Entry.grid(row=13, column=3)

        self.portata3_out=tk.Entry(self.FinesScambioQ)
        self.portata3_out.grid(row=14, column=3)

        #empty row
        empty_label3 = tk.Label(self.FinesScambioQ, text="")
        empty_label3.grid(row=15, column=0)
        # OK Button
        self.ok_button_chisura = tk.Button(
            self.FinesScambioQ,
            text="Calcola",
            font=("Helvetica", 10, "bold"),
            bg="light blue",
            command=self.close_window  # replace with the function to be executed
)
        self.ok_button_chisura.grid(row=16, column=1)

        self.closeButtonQ = tk.Button(self.FinesScambioQ, 
                                    text="Chiudi",
                                    font=("Helvetica", 10, "bold"),
                                    bg="orange",
                                    command=lambda: self.distruggi(self.FinesScambioQ))
        self.closeButtonQ.grid(row=16, column=3)

    def FluidoOUT(self, fluido_out):
        self.InserimentoFluidoOut = tk.Toplevel(self.root)
        self.InserimentoFluidoOut.title("Inserimento Fluido")
        self.InserimentoFluidoOut.geometry("420x270")

        self.LabelFluido = tk.Label(self.InserimentoFluidoOut,
                                    text="Inserisci la composizione del fluido",
                                    font=("Helvetica", 12, "bold"),
                                    fg="green")
        self.LabelFluido.grid(row=0, column=0, columnspan=2)

        #empty row
        self.riga_vuota = tk.Label(self.InserimentoFluidoOut, text="")
        self.riga_vuota.grid(row=1, column=0)

        # Crea una StringVar per ogni Entry
        try:
            self.QuantitaFC1_out_var = tk.StringVar()
            self.QuantitaFC2_out_var = tk.StringVar()
            self.QuantitaFC3_out_var = tk.StringVar()
            self.QuantitaFC4_out_var = tk.StringVar()
            self.QuantitaFC5_out_var = tk.StringVar()
        except AttributeError:
            print("Errore")

        # Crea una lista di StringVars
        self.Quantita_vars = [self.QuantitaFC1_out_var,
                            self.QuantitaFC2_out_var,
                            self.QuantitaFC3_out_var,
                            self.QuantitaFC4_out_var,
                            self.QuantitaFC5_out_var]

        # Crea una Entry per ogni StringVar
        self.QuantitaFC1_out = tk.Entry(self.InserimentoFluidoOut, 
                                        textvariable=self.QuantitaFC1_out_var)
        self.QuantitaFC1_out.grid(row=2, column=1)
        
        self.QuantitaFC2_out = tk.Entry(self.InserimentoFluidoOut,
                                    textvariable=self.QuantitaFC2_out_var)
        self.QuantitaFC2_out.grid(row=3, column=1)

        self.QuantitaFC3_out = tk.Entry(self.InserimentoFluidoOut,
                                        textvariable=self.QuantitaFC3_out_var)
        self.QuantitaFC3_out.grid(row=4, column=1)

        self.QuantitaFC4_out = tk.Entry(self.InserimentoFluidoOut, 
                                        textvariable=self.QuantitaFC4_out_var)
        self.QuantitaFC4_out.grid(row=5, column=1)

        self.QuantitaFC5_out = tk.Entry(self.InserimentoFluidoOut, 
                                        textvariable=self.QuantitaFC5_out_var)
        self.QuantitaFC5_out.grid(row=6, column=1)

        self.FluidoC1_out = AutocompleteCombobox(self.InserimentoFluidoOut)
        self.FluidoC1_out.set_completion_list(self.fluids)
        self.FluidoC1_out.grid(row=2, column=0)

        self.FluidoC2_out=AutocompleteCombobox(self.InserimentoFluidoOut)
        self.FluidoC2_out.set_completion_list(self.fluids)
        self.FluidoC2_out.grid(row=3, column=0)

        self.FluidoC3_out=AutocompleteCombobox(self.InserimentoFluidoOut)
        self.FluidoC3_out.set_completion_list(self.fluids)
        self.FluidoC3_out.grid(row=4, column=0)

        self.FluidoC4_out=AutocompleteCombobox(self.InserimentoFluidoOut)
        self.FluidoC4_out.set_completion_list(self.fluids)
        self.FluidoC4_out.grid(row=5, column=0)

        self.FluidoC5_out=AutocompleteCombobox(self.InserimentoFluidoOut)
        self.FluidoC5_out.set_completion_list(self.fluids)
        self.FluidoC5_out.grid(row=6, column=0)

        # Crea la label rimanenza
        self.rimanenza = tk.Label(self.InserimentoFluidoOut,
                                text='1',
                                font=("Helvetica", 10, "bold"))
        self.rimanenza.grid(row=6, column=3)

        # Chiama aggiorna_rimanenza ogni volta che una StringVar cambia
        for quantita_var in self.Quantita_vars:
            quantita_var.trace('w', self.aggiorna_rimanenza)

        self.ok_button_out = tk.Button(self.InserimentoFluidoOut,
                                        text="Inserisci",
                                        font=("Helvetica", 10, "bold"),
                                        bg="#D3D3D3",
                                        command=lambda: self.SalvataggioFluidoOUT(fluido_out))
        self.ok_button_out.grid(row=10, column=1)
        self.ok_button_out.bind('<Button-1>', lambda event: self.cambia_colore(fluido_out))
        
    def SalvataggioFluidoOUT(self, fluido_out):
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
            SpecieChimiche_out = [comp for comp in SpecieChimiche_out if comp]
            Quantita_out = [qty for qty in Quantita_out if qty]
            mixture_out = "&".join(f"{comp}[{qty}]" for comp, qty in zip(SpecieChimiche_out, Quantita_out))
            if fluido_out == "Fluido1_OUT":
                self.mixture_out1_var.set(mixture_out)
            elif fluido_out == "Fluido2_OUT":
                self.mixture_out2_var.set(mixture_out)
            elif fluido_out == "Fluido3_OUT":
                self.mixture_out3_var.set(mixture_out)
        except AttributeError:
            print("Errore")
        finally:
            getattr(self.InserimentoFluidoOut, 'destroy', lambda: None)()

    def FluidoIN(self, fluido_in):
        self.InserimentoFluido = tk.Toplevel(self.root)
        self.InserimentoFluido.title("Inserimento Fluido")
        self.InserimentoFluido.geometry("420x270")

        self.LabelFluido = tk.Label(self.InserimentoFluido,
                                    text="Inserisci la composizione del fluido",
                                    font=("Helvetica", 12, "bold"),
                                    fg="blue")
        self.LabelFluido.grid(row=0, column=0, columnspan=2)

        # Crea una StringVar per ogni Entry
        try:
            self.QuantitaFC1_var = tk.StringVar()
            self.QuantitaFC2_var = tk.StringVar()
            self.QuantitaFC3_var = tk.StringVar()
            self.QuantitaFC4_var = tk.StringVar()
            self.QuantitaFC5_var = tk.StringVar()
        except AttributeError:
            print("Errore")
        # Crea una lista di StringVars
        self.Quantita_vars = [self.QuantitaFC1_var,
                            self.QuantitaFC2_var,
                            self.QuantitaFC3_var,
                            self.QuantitaFC4_var,
                            self.QuantitaFC5_var]

        # empty row
        self.riga_vuota = tk.Label(self.InserimentoFluido, text="")
        self.riga_vuota.grid(row=1, column=0)

        # Crea una Entry per ogni StringVar
        self.QuantitaFC1 = tk.Entry(self.InserimentoFluido, 
                                    textvariable=self.QuantitaFC1_var)
        self.QuantitaFC1.grid(row=2, column=1)

        self.QuantitaFC2 = tk.Entry(self.InserimentoFluido,
                                    textvariable=self.QuantitaFC2_var)
        self.QuantitaFC2.grid(row=3, column=1)

        self.QuantitaFC3 = tk.Entry(self.InserimentoFluido, 
                                    textvariable=self.QuantitaFC3_var)
        self.QuantitaFC3.grid(row=4, column=1)

        self.QuantitaFC4 = tk.Entry(self.InserimentoFluido, 
                                    textvariable=self.QuantitaFC4_var)
        self.QuantitaFC4.grid(row=5, column=1)

        self.QuantitaFC5 = tk.Entry(self.InserimentoFluido, 
                                    textvariable=self.QuantitaFC5_var)
        self.QuantitaFC5.grid(row=6, column=1)

        # self.FluidoC1=ttk.Combobox(self.InserimentoFluido, 
        #                         values=self.fluids)
        # self.FluidoC1.grid(row=2, column=0)
        self.FluidoC1 = AutocompleteCombobox(self.InserimentoFluido)
        self.FluidoC1.set_completion_list(self.fluids)
        self.FluidoC1.grid(row=2, column=0)

        self.FluidoC2= AutocompleteCombobox(self.InserimentoFluido)
        self.FluidoC2.set_completion_list(self.fluids)
        self.FluidoC2.grid(row=3, column=0)

        self.FluidoC3= AutocompleteCombobox(self.InserimentoFluido)
        self.FluidoC3.set_completion_list(self.fluids)
        self.FluidoC3.grid(row=4, column=0)

        self.FluidoC4= AutocompleteCombobox(self.InserimentoFluido)
        self.FluidoC4.set_completion_list(self.fluids)
        self.FluidoC4.grid(row=5, column=0)

        self.FluidoC5= AutocompleteCombobox(self.InserimentoFluido)
        self.FluidoC5.set_completion_list(self.fluids)
        self.FluidoC5.grid(row=6, column=0)

        # Crea la label rimanenza
        self.rimanenza = tk.Label(self.InserimentoFluido,
                                text='1',
                                font=("Helvetica", 10, "bold"))
        self.rimanenza.grid(row=6, column=3)

        # Chiama aggiorna_rimanenza ogni volta che una StringVar cambia
        for quantita_var in self.Quantita_vars:
            quantita_var.trace('w', self.aggiorna_rimanenza)

        self.ok_button = tk.Button(self.InserimentoFluido,
                                    text="Inserisci", 
                                    font=("Helvetica", 10, "bold"),
                                    bg="#D3D3D3",
                                    command=lambda: self.SalvataggioFluidoIN(fluido_in))
        self.ok_button.grid(row=10, column=1)
        self.ok_button.bind('<Button-1>', lambda event: self.cambia_colore(fluido_in))

    def aggiorna_rimanenza(self, *args):
        Quantita_non_vuoti = []

        for quantita_var in self.Quantita_vars:
            valore = quantita_var.get()
            if valore != '':
                Quantita_non_vuoti.append(float(valore))

        rimanenza = 1 - sum(Quantita_non_vuoti)

        self.rimanenza.config(text=rimanenza)

    def SalvataggioFluidoIN(self,fluido_in):
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
            SpecieChimiche = [comp for comp in SpecieChimiche if comp]
            Quantita = [qty for qty in Quantita if qty]
            mixtu = "&".join(f"{comp}[{qty}]" for comp, qty in zip(SpecieChimiche, Quantita))
            if fluido_in == "Fluido1_IN":
                self.mixture_in1_var.set(mixtu)
            elif fluido_in == "Fluido2_IN":
                self.mixture_in2_var.set(mixtu)
            elif fluido_in == "Fluido3_IN":
                self.mixture_in3_var.set(mixtu)
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

    def SalvataggioFluidoTSat(self):
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
            SpecieChimiche=[self.Fluido1, 
                            self.Fluido2, 
                            self.Fluido3,
                            self.Fluido4, 
                            self.Fluido5]
            Quantita=[self.Quantita1,
                    self.Quantita2, 
                    self.Quantita3, 
                    self.Quantita4, 
                    self.Quantita5]
            key = f"Fluido_{len(self.fluido_results_in) + 1}"
            self.fluido_results_in[key] = (SpecieChimiche, Quantita)
                # Unisci i componenti e le quantità in una stringa di miscela
            self.mixtureTsat='&'.join([f"{comp}[{qty}]" for comp, qty in zip(SpecieChimiche, Quantita) if comp and qty])
            print(f"{key}: {self.mixtureTsat}")
            fluido=self.mixtureTsat
            p=self.Pressione_Tsat.get()
            try:
                Tsat=self.calculate_Tsat(fluido, p)
                messagebox.showinfo("Risultato", f"Temperatura di Saturazione [°C]: {Tsat}")
            except ValueError:
                messagebox.showinfo("Errore", "Condizioni non coperte dal databse")
            finally:
                self.FinesCondizioniSaturazione.destroy()
        except AttributeError:
            print("Errore")

    def close_window_Tsat(self):
        fluido=self.mixtureTsat
        p=self.Pressione_Tsat.get()
        try:
            Tsat=self.calculate_Tsat(fluido, p)
            messagebox.showinfo("Risultato", f"Temperatura di Saturazione [°C]: {Tsat}")
        except ValueError:
            messagebox.showinfo("Errore", "Condizioni non coperte dal databse")

            # self.FinesCondizioniSaturazione.destroy()

    def calculate_Tsat(self,fluido, p):
        from CoolProp.CoolProp import PropsSI
        p=(float(p)+1)*1e5
        Tsat=PropsSI('T', 'P', p, 'Q', 0, fluido)
        return Tsat-273.15

    def FinestraPsat(self):
        self.FinesPsat = tk.Toplevel(self.root)
        self.FinesPsat.title("Finestra Pressione di Saturazione")
        self.FinesPsat.geometry("450x270")

        # TITOLO
        self.label_titolo= tk.Label(self.FinesPsat, 
                                    text="Calcolo della pressione di saturazione della miscela",
                                    font=("Helvetica", 12, "bold"),fg="red")
        self.label_titolo.grid(row=0, column=0, columnspan=2)

        #riga vuota
        self.riga_vuota = tk.Label(self.FinesPsat,
                                    text="")
        self.riga_vuota.grid(row=1, column=0)

        #titolo inserisci pressione
        self.label_temperatura = tk.Label(self.FinesPsat,
                                        text="Inserisci la temperatura [°C]",
                                        font=("Helvetica", 12, "bold"))
        self.label_temperatura.grid(row=2, column=0)
        # Inserisci la pressione
        self.Temperatura_Psat = tk.Entry(self.FinesPsat)
        self.Temperatura_Psat.grid(row=2, column=1)

        self.LabelFluido = tk.Label(self.FinesPsat, 
                                    text="Inserisci la composizione del fluido: base molare",
                                    font=("Helvetica", 12, "bold"))
        self.LabelFluido.grid(row=3, column=0, columnspan=2)

        # Crea una StringVar per ogni Entry
        try:
            self.QuantitaFC1_var = tk.StringVar()
            self.QuantitaFC2_var = tk.StringVar()
            self.QuantitaFC3_var = tk.StringVar()
            self.QuantitaFC4_var = tk.StringVar()
            self.QuantitaFC5_var = tk.StringVar()
        except AttributeError:
            print("Errore")

        # Crea una lista di StringVars
        self.Quantita_vars = [self.QuantitaFC1_var, 
                            self.QuantitaFC2_var, 
                            self.QuantitaFC3_var, 
                            self.QuantitaFC4_var, 
                            self.QuantitaFC5_var]

        # Crea una Entry per ogni StringVar
        self.QuantitaFC1 = tk.Entry(self.FinesPsat, 
                                    textvariable=self.QuantitaFC1_var)
        self.QuantitaFC1.grid(row=4, column=1)

        self.QuantitaFC2 = tk.Entry(self.FinesPsat,
                                textvariable=self.QuantitaFC2_var)
        self.QuantitaFC2.grid(row=5, column=1)

        self.QuantitaFC3 = tk.Entry(self.FinesPsat, 
                                    textvariable=self.QuantitaFC3_var)
        self.QuantitaFC3.grid(row=6, column=1)

        self.QuantitaFC4 = tk.Entry(self.FinesPsat, 
                                    textvariable=self.QuantitaFC4_var)
        self.QuantitaFC4.grid(row=7, column=1)

        self.QuantitaFC5 = tk.Entry(self.FinesPsat,
                                    textvariable=self.QuantitaFC5_var)
        self.QuantitaFC5.grid(row=8, column=1)

        self.FluidoC1=ttk.Combobox(self.FinesPsat,
                                values=self.fluids)
        self.FluidoC1.grid(row=4, column=0)

        self.FluidoC2=ttk.Combobox(self.FinesPsat,
                                values=self.fluids)
        self.FluidoC2.grid(row=5, column=0)

        self.FluidoC3=ttk.Combobox(self.FinesPsat,
                                    values=self.fluids)
        self.FluidoC3.grid(row=6, column=0)

        self.FluidoC4=ttk.Combobox(self.FinesPsat,
                                    values=self.fluids)
        self.FluidoC4.grid(row=7, column=0)

        self.FluidoC5=ttk.Combobox(self.FinesPsat,
                                    values=self.fluids)
        self.FluidoC5.grid(row=8, column=0)

        self.rimanenza = tk.Label(self.FinesPsat,
                                text='1')
        self.rimanenza.grid(row=8, column=3)

        # Chiama aggiorna_rimanenza ogni volta che una StringVar cambia
        for quantita_var in self.Quantita_vars:
            quantita_var.trace('w', self.aggiorna_rimanenza)

        self.ok_button = tk.Button(self.FinesPsat, 
                                text="Calcola", 
                                font=("Helvetica", 10, "bold"),
                                bg="#D3D3D3",
                                command=self.SalvataggioFluidopSat)
        self.ok_button.grid(row=9, column=0)

        self.closeButtonp = tk.Button(self.FinesPsat, 
                                    text="Chiudi", 
                                    font=("Helvetica", 10, "bold"),
                                    bg="#D3D3D3",
                                    command=lambda: self.distruggi(self.FinesPsat))
        self.closeButtonp.grid(row=9, column=1)

    def SalvataggioFluidopSat(self):
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
        except AttributeError:
            print("Errore")

        SpecieChimiche=[self.Fluido1,
                        self.Fluido2,
                        self.Fluido3,
                        self.Fluido4,
                        self.Fluido5]
        Quantita=[self.Quantita1,
                self.Quantita2,
                self.Quantita3,
                self.Quantita4,
                self.Quantita5]
        key = f"Fluido_{len(self.fluido_results_in) + 1}"
        self.fluido_results_in[key] = (SpecieChimiche, Quantita)
            # Unisci i componenti e le quantità in una stringa di miscela
        self.mixturePsat='&'.join([f"{comp}[{qty}]" for comp, qty in zip(SpecieChimiche, Quantita) if comp and qty])
        print(f"{key}: {self.mixturePsat}")
        fluido=self.mixturePsat
        T=self.Temperatura_Psat.get()
        try:
            Psat=self.calculate_Psat(fluido, T)
            messagebox.showinfo("Risultato", f"Pressione di Saturazione [barg]: {Psat}")
        except ValueError:
            messagebox.showinfo("Errore", "Condizioni non coperte dal databse")

    def calculate_Psat(self,fluido, T):
        from CoolProp.CoolProp import PropsSI
        try:
            T=float(T)+273.15
            Psat=PropsSI('P', 'T', T, 'Q', 0, fluido)*1e-5
            return Psat
        except Exception as e:
            return None

    def close_window(self):
        try:
            self.T1_in = self.T1_in_Entry.get()
            self.P1_in = self.P1_in_Entry.get()
            self.portata1 = self.portata1.get()
            self.T1_out = self.T1_out_Entry.get()
            self.P1_out = self.P1_out_Entry.get()
            self.portata1_out = self.portata1_out.get()
            self.T2_in = self.T2_in_Entry.get()
            self.P2_in = self.P2_in_Entry.get()
            self.portata2 = self.portata2.get()
            self.T2_out = self.T2_out_Entry.get()
            self.P2_out = self.P2_out_Entry.get()
            self.portata2_out = self.portata2_out.get()
            self.T3_in = self.T3_in_Entry.get()
            self.P3_in = self.P3_in_Entry.get()
            self.portata3 = self.portata3.get()
            self.T3_out = self.T3_out_Entry.get()
            self.P3_out = self.P3_out_Entry.get()
            self.portata3_out = self.portata3_out.get()
            self.mixture_in1 = self.mixture_in1_var.get()
            self.mixture_in2 = self.mixture_in2_var.get()
            self.mixture_in3 = self.mixture_in3_var.get()
            self.mixture_out1 = self.mixture_out1_var.get()
            self.mixture_out2 = self.mixture_out2_var.get()
            self.mixture_out3 = self.mixture_out3_var.get()

        except AttributeError:
            print("Errore nell'import dei dati T,p,m da finestra")
        try:
            Q_Scambiato=self.calcolo_H()
            messagebox.showinfo("Risultato", f"Q Scambiato [kW]: {Q_Scambiato}")
        except ValueError:
            messagebox.showinfo("Errore", "Condizioni non coperte dal databse")

    def calculate_h(self,fluido, p, T):
        from CoolProp.CoolProp import PropsSI
        try:
            p=(float(p)+1)*10**5
            T=float(T)+273.15
            h = PropsSI('H', 'P', p, 'T', T, fluido)
            return h/1000
        except Exception as e:
            return None
    
    def calculate_Q(self,h_in,m_in,h_out,m_out):
        try:
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
        except Exception as e:
            return None

    def calcolo_H(self):
        try:
            mixture_in = []
            mixture_out = []
            p_in = []
            T_in = []
            m_in = []
            p_out = []
            T_out = []
            m_out = []
            h_in = []
            h_out = []
            mixture_in = [self.mixture_in1, self.mixture_in2, self.mixture_in3]
            mixture_out = [self.mixture_out1, self.mixture_out2, self.mixture_out3]
            p_in = [self.P1_in, self.P2_in, self.P3_in]
            T_in = [self.T1_in, self.T2_in, self.T3_in]
            m_in = [self.portata1, self.portata2, self.portata3]
            p_out = [self.P1_out, self.P2_out, self.P3_out]
            T_out = [self.T1_out, self.T2_out, self.T3_out]
            m_out = [self.portata1_out, self.portata2_out, self.portata3_out]
            #pulisci dei valori vuputi
            p_in = [p for p in p_in if p]
            T_in = [T for T in T_in if T]
            m_in = [m for m in m_in if m]
            p_out = [p for p in p_out if p]
            T_out = [T for T in T_out if T]
            m_out = [m for m in m_out if m]
            mixture_in = [m for m in mixture_in if m]
            mixture_out = [m for m in mixture_out if m]
        
        except AttributeError:
            print("Errore nell'import dei dati per il calcolo di H")

        # for fluid_name, fluid_data in self.get_fluido_results_in().items():
        #     components, quantities, pressure, temperature, portata = fluid_data
        #     p_in.append(pressure)
        #     T_in.append(temperature)
        #     m_in.append(portata)
        #     # Unisci i componenti e le quantità in una stringa di miscela
        #     mixture_in.append("&".join(f"{comp}[{qty}]" for comp, qty in zip(components, quantities) if comp and qty))
        
        # for fluid_name, fluid_data in self.get_fluido_results_out().items():
        #     components, quantities, pressure, temperature, portata = fluid_data
        #     p_out.append(pressure)
        #     T_out.append(temperature)
        #     m_out.append(portata)
        #     # Unisci i componenti e le quantità in una stringa di miscela
        #     mixture_out.append("&".join(f"{comp}[{qty}]" for comp, qty in zip(components, quantities) if comp and qty))

        for i, element in enumerate(m_in):
            h_in.append(self.calculate_h(mixture_in[i], p_in[i], T_in[i]))

        for i, element in enumerate(m_out):
            h_out.append(self.calculate_h(mixture_out[i], p_out[i], T_out[i]))

        QScambiatore=self.calculate_Q(h_in,m_in,h_out,m_out)
        return QScambiatore
    
    def distruggi(self,finestra):
        finestra.destroy()