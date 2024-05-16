import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from CoolProp.CoolProp import FluidsList

class Interfaccia:
        
    def __init__(self,root):
        self.root = root
        self.fluids = FluidsList()
        self.fluido_results = {}
        

    def FinestraPrincipale(self):
        self.root.title("Finestra Principale")
        self.root.geometry("500x300")
        
        # TITOLO
        self.label_titolo= tk.Label(self.root, text="Calcolo delle proprietà termodinamiche dei fluidi")
        self.label_titolo.grid(row=0, column=0)

        # Fluidi input
        self.label_file_in= tk.Label(self.root, text="Fluidi in input")
        self.label_file_in.grid(row=1, column=0)
        
        # Fluido 1
        self.fluido_in1 = tk.Button(
                            self.root,
                            text="Fluido1",
                            command=self.Fluido)
        self.fluido_in1.grid(row=2, column=0)

                # Fluido 2
        self.fluido_in2 = tk.Button(
                            self.root,
                            text="Fluido2",
                            command=self.Fluido)
        self.fluido_in2.grid(row=3, column=0)

        # Fluido 3
        self.fluido_in3 = tk.Button(
                            self.root,
                            text="Fluido3",
                            command=self.Fluido)
        self.fluido_in3.grid(row=4, column=0)

    def Fluido(self):
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

        # Crea la label rimanenza
        self.rimanenza = tk.Label(self.InserimentoFluido, text='1')
        self.rimanenza.grid(row=6, column=3)

        # Chiama aggiorna_rimanenza ogni volta che una StringVar cambia
        for quantita_var in self.Quantita_vars:
            quantita_var.trace('w', self.aggiorna_rimanenza)

        self.ok_button = tk.Button(self.InserimentoFluido, text="OK", command=self.SalvataggioFluido)
        self.ok_button.grid(row=8, column=1)

    def aggiorna_rimanenza(self, *args):
        Quantita_non_vuoti = []

        for quantita_var in self.Quantita_vars:
            valore = quantita_var.get()
            if valore != '':
                Quantita_non_vuoti.append(float(valore))

        rimanenza = 1 - sum(Quantita_non_vuoti)

        self.rimanenza.config(text=rimanenza)

    def SalvataggioFluido(self):
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
            SpecieChimiche=[self.Fluido1, self.Fluido2, self.Fluido3, self.Fluido4, self.Fluido5]
            Quantita=[self.Quantita1, self.Quantita2, self.Quantita3, self.Quantita4, self.Quantita5]
            key = f"Fluido_{len(self.fluido_results) + 1}"
            self.fluido_results[key] = (SpecieChimiche, Quantita, self.Pressione, self.Temperatura)
            # Stampa le condizioni appena salvate
            print(f"Condizioni per {key}: {self.fluido_results[key]}")
        except AttributeError:
            print("Errore")
        finally:
            getattr(self.InserimentoFluido, 'destroy', lambda: None)()

    def get_fluido_results(self):
        return self.fluido_results




    #     # STATISTICHE
    #     self.pulsante_statistiche = tk.Button(
    #                         self.root,
    #                         text="Statistiche",
    #                         command=self.FinestraStatistiche)
    #     self.pulsante_statistiche.grid(row=2, column=1)

    #     # SALVATAGGIO
    #     # Label per mostrare il percorso di salvataggio
    #     self.save_label = tk.Label(self.root, text="Nessuna cartella di salvataggio selezionata")
    #     self.save_label.grid(row=5, column=1, padx=10, pady=10)

    #     # Bottone per sfogliare le cartelle di salvataggio
    #     self.save_button = tk.Button(self.root, text="Sfoglia", command=self.save_in)
    #     self.save_button.grid(row=5, column=2, padx=10, pady=10)

    #         # Label per mostrare il percorso di salvataggio
    #     self.FileName = tk.Label(self.root, text="Nome file finale:")
    #     self.FileName.grid(row=5, column=3, padx=10, pady=10)

    #     # Entry per inserire il nome del file
    #     self.file_nameC = tk.Entry(self.root)
    #     self.file_nameC.grid(row=5, column=4, padx=10, pady=10)
    #     self.OpzSalva=tk.BooleanVar()
    #     self.pulsante_salva = tk.Checkbutton(
    #         self.root,
    #         text="Salva",
    #         variable=self.OpzSalva)
    #     self.pulsante_salva.grid(row=3, column=0)

    #     # Bottone OK
    #     self.ok_button = tk.Button(self.root, text="OK", command=self.Salvataggio)
    #     self.ok_button.grid(row=4, column=2, padx=10, pady=10)

    #     self.filepath = ""
    #     self.save_path = ""
    #     self.FileName = ""

    # def file_input_sfoglia(self):
    #     ####
    #     # SELEZIONE DEL FILE E CARICAMENTO DEI DATI
    #     ####
    #     from . import AperturaFile
    #     self.path_in = filedialog.askopenfilename()
    #     if self.path_in:  # Aggiorna il Label solo se è stato selezionato un file
    #         self.label_file_in.config(text=self.path_in)
    #         self.df=AperturaFile(self.path_in).Apertura() #se cambia il formato vai in AperuraFile e aggiungi la funzione di conversione da file a dataframe
    #         self.tempo=list(self.df['Data'].unique())
    #         print(self.df['Data'])

    # def FinestraFiltro(self):
    #     self.finestra_filtro = tk.Toplevel(self.root)
    #     self.finestra_filtro.title("Finestra Filtro")
    #     self.finestra_filtro.geometry("1000x200")

    #     # Creazione delle variabili per i Checkbutton
    #     self.IntervalloT = tk.BooleanVar()
    #     self.IntervalloT.trace('w', self.update_checkboxes)
    #     self.DaTempo = tk.BooleanVar()
    #     self.DaTempo.trace('w', self.update_checkboxes)

    #     # SEZIONE FILTRO
    #     self.testoFiltro = tk.Label(self.finestra_filtro, text="Seleziona la tipologia di filtro")
    #     self.testoFiltro.grid(row=0, column=0)
    #     # FILTRO INTERVALLO DI TEMPO
    #     # TEMPO INIZIO
    #     self.checkFiltro1 = tk.Checkbutton(self.finestra_filtro, text="Intervallo di tempo", variable=self.IntervalloT)
    #     self.checkFiltro1.grid(row=1, column=0)
    #     self.TempoInizio = tk.Label(self.finestra_filtro, text="Tempo di inizio")
    #     self.TempoInizio.grid(row=1, column=2)
    #     self.tempoIN = tk.StringVar()
    #     self.Tin = ttk.Combobox(self.finestra_filtro, textvariable=self.tempoIN)  # Usa ttk.Combobox invece di tk.OptionMenu
    #     self.Tin['values'] = self.tempo  # Imposta i valori del Combobox
    #     self.Tin.grid(row=1, column=3)
    #     # TEMPO FINE
    #     self.TempoFine = tk.Label(self.finestra_filtro, text="Tempo di fine")
    #     self.TempoFine.grid(row=1, column=5)
    #     self.tempoFIN = tk.StringVar()
    #     self.Tfin = ttk.Combobox(self.finestra_filtro, textvariable=self.tempoFIN)
    #     self.Tfin['values'] = self.tempo
    #     self.Tfin.grid(row=1, column=6)
    #     # FILTRO SCARTO INIZIALE TEMPORALE
    #     self.Filtro2 = tk.Checkbutton(self.finestra_filtro, text="Scarto Iniziale", variable=self.DaTempo)
    #     self.Filtro2.grid(row=3, column=0)
    #     self.TempoDa = tk.Label(self.finestra_filtro, text="Tempo d'inizio")
    #     self.TempoDa.grid(row=3, column=1)
    #     self.tempoDa=tk.StringVar()
    #     self.TDa=ttk.Combobox(self.finestra_filtro, textvariable=self.tempoDa)
    #     self.TDa['values']=self.tempo
    #     self.TDa.grid(row=3, column=2)
    #     # BOTTONE OK E CHIUSURA
    #     self.ok_button = tk.Button(self.finestra_filtro, text="OK", command=self.SalvataggioFiltro)
    #     self.ok_button.grid(row=4, column=2, padx=10, pady=10)

    # def update_checkboxes(self, *args):
    #     if self.IntervalloT.get():
    #         self.Filtro2.config(state='disabled')
    #     elif self.DaTempo.get():
    #         self.checkFiltro1.config(state='disabled')
    #     else:
    #         self.checkFiltro1.config(state='normal')
    #         self.Filtro2.config(state='normal')
    
    # def SalvataggioFiltro(self):
    #     try:
    #         # checkbox filtro intervallo di tempo
    #         self.FiltroIntervallo=self.IntervalloT.get() 
    #         # checkbox filtro scarto iniziale
    #         self.Filtro2=self.DaTempo.get()
            
    #         if (self.IntervalloT.get()==True and
    #             self.Tin.get() and
    #             self.Tfin.get()):
    #             # se sono in intervallo e i menu sono compilati
    #             self.TempoIniziale=self.Tin.get()
    #             print(self.TempoIniziale)
    #             self.TempoFinale=self.tempoFIN.get()
    #             print(self.TempoFinale)
    #         elif (self.Filtro2==True and self.TDa.get()):
    #             self.TempoDa=self.TDa.get() 
    #     except AttributeError:
    #         print("Errore: Il filtro non è stato ancora applicato.")
    #     finally:
    #         getattr(self.finestra_filtro, 'destroy', lambda: None)()  # Chiude la finestra secondaria

    # def Salvataggio(self):  
    #     try:
    #         self.OpzSalvaS=self.OpzSalva.get()
    #         self.file_name = self.file_nameC.get()
    #         if not self.FileName:  # Check if file_name is empty
    #             self.FileName = self.filenameD  # Assign a default file name
    #         if not self.save_path:
    #             self.save_path = self.filepathD
    #         self.savename = self.save_path + '/' + self.FileName + '_' + self.current_time +  ".xlsx"
    #         self.savename = self.savename.replace("/", '\\')
    #     except AttributeError:
    #         print("Errore")
    #     finally:
    #         getattr(self.root, 'destroy', lambda: None)()

    # def FinestraStatistiche(self):
    #     self.finestra_stat = tk.Toplevel(self.root)
    #     self.finestra_stat.title("Finestra Statistiche")
    #     self.finestra_stat.geometry("1000x200")

    #     # CREAZIONE DELLE VARIABILI PER I CHECKBUTTON
    #     self.Media_var = tk.BooleanVar()
    #     self.Mediana_var = tk.BooleanVar()
    #     self.Moda_var = tk.BooleanVar()
    #     self.Deviazione_var = tk.BooleanVar()
    #     self.Varianza_var = tk.BooleanVar()
    #     self.minimo_var = tk.BooleanVar()
    #     self.massimo_var = tk.BooleanVar()
    #     self.Dati_grezzi_var = tk.BooleanVar()
    #     self.Dati_filtrati_var = tk.BooleanVar()

    #     # SEZIONE STATISTICHE
    #     self.testoStat = tk.Label(self.finestra_stat,
    #                         text="Seleziona la tipologia di statistica",
    #                         font=("Helvetica", 10, "bold"))
    #     self.testoStat.grid(row=0, column=0)
    #     # STATISTICA: MEDIA
    #     self.Media = tk.Checkbutton(self.finestra_stat, text="Media", variable=self.Media_var)
    #     self.Media.grid(row=1, column=0)
    #     # STATISTICA: MEDIANA
    #     self.Mediana = tk.Checkbutton(self.finestra_stat, text="Mediana", variable=self.Mediana_var)
    #     self.Mediana.grid(row=2, column=0)
    #     # STATISTICA: MODA
    #     self.Moda = tk.Checkbutton(self.finestra_stat, text="Moda", variable=self.Moda_var)
    #     self.Moda.grid(row=3, column=0)
    #     # STATISTICA: DEVIAZIONE STANDARD
    #     self.Deviazione = tk.Checkbutton(self.finestra_stat, text="Deviazione Standard", variable=self.Deviazione_var)
    #     self.Deviazione.grid(row=4, column=0)
    #     # STATISTICA: VARIANZA
    #     self.Varianza = tk.Checkbutton(self.finestra_stat, text="Varianza", variable=self.Varianza_var)
    #     self.Varianza.grid(row=5, column=0)
    #     # STATISTICA: MINIMO
    #     self.Minimo = tk.Checkbutton(self.finestra_stat, text="Minimo", variable=self.minimo_var)
    #     self.Minimo.grid(row=6, column=0)
    #     # STATISTICA: MASSIMO
    #     self.Massimo = tk.Checkbutton(self.finestra_stat, text="Massimo", variable=self.massimo_var)
    #     self.Massimo.grid(row=7, column=0)

    #     # SELEZIONA DATI    
    #     self.SelezionaDati = tk.Label(self.finestra_stat, 
    #                 text="Seleziona i dati su cui fare le statistiche",
    #                 font=("Helvetica", 10, "bold"))
        
    #     self.SelezionaDati.grid(row=0, column=2)
    #     self.Dati_grezzi = tk.Checkbutton(self.finestra_stat, text="Dati grezzi", variable=self.Dati_grezzi_var)
    #     self.Dati_grezzi.grid(row=1, column=2)
    #     self.Dati_filtrati = tk.Checkbutton(self.finestra_stat, text="Dati filtrati", variable=self.Dati_filtrati_var)
    #     self.Dati_filtrati.grid(row=2, column=2)


    #     # BOTTONE OK E CHIUSURA
    #     self.ok_button_stat = tk.Button(self.finestra_stat, text="OK", command=self.SalvataggioStat)
    #     self.ok_button_stat.grid(row=4, column=2, padx=10, pady=10)

    # def SalvataggioStat(self):
    #     try:
    #         self.MediaS=self.Media_var.get()
    #         self.MedianaS=self.Mediana_var.get()
    #         self.ModaS=self.Moda_var.get()
    #         self.DeviazioneS=self.Deviazione_var.get()
    #         self.VarianzaS=self.Varianza_var.get()
    #         self.minimoS=self.minimo_var.get()
    #         self.massimoS=self.massimo_var.get()
    #         self.Dati_grezziS=self.Dati_grezzi_var.get()
    #         self.Dati_filtratiS=self.Dati_filtrati_var.get()
    #     except AttributeError:
    #         print("Errore")
    #     finally:
    #         getattr(self.finestra_stat, 'destroy', lambda: None)()

    # def save_in(self):
    #     # Apri il dialogo per selezionare la directory
    #     self.save_path = filedialog.askdirectory()
    #     if self.save_path:
    #         self.save_label.config(text=f"Salva in: {self.save_path}")