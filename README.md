# ScambiatoreCalore

Questo codice permette di calcolare lo scambio termico che avviene conoscendo composizione, temperatura, pressione e portata del fluidi in ingresso e in uscita (nel caso sia lo scambio fra più fluidi il bilancio lo si fa su un fluido).

Permette anche di calcolare:

* Temperatura di saturazione, conoscendo la pressione e la composizione
* Pressione di saturazione, conoscendo la temperatura e la composizione
* Composizione di saturazione, conoscendo temperatura e pressione

LIBRERIE NECESSARIE

1) CoolProp -> pip install CoolProp

 BREVE GUIDA

1) Run
   **PER CALCOLARE LO SCAMBIO TERMICO:**
2) Selezionare il bottone "Scambio Termico"
3) Clicare sul bottone per inserie i fluidi -> si apre una nuova finestra con diversi campi da riempire
4) Nei menù a tendina ci sono i fluidi a disposizione nella libreria
5) Accanto ad oni specie chimica specificare la composizone molare (in numero NON in percntuale). Accanto all'ultima c'è scrit quanto manca per arrivare ad un valore unitario !!!! FONDAMENTALE che non si superi il valore unitario o da errore
6) Inserie T,p e portata massiaca (nelle unità di misura indicate)
7) cliccare "Inserisci", si chiude questa schemata -> verificare che il bottone precedentemente premuto sia diventato verde
8) fare le stesse operazioni per i fluidi necessari
9) cliccare "Calcola", tiene in memeoria i fluidi utilizzati perciò se si vuole cambiare un fluido va premuto sul fluido da cambiare se invece se ne vuole aggiungere va cliccato un bottone libero
10) Una volta conclusi i calcolo cliccare "Chiudi"

    **PER CALCOLARE LE PROPRIETà DI SATURAZIONE**
11) Cliccare "Condizioni di Saturazione"
12) Scegliere la proprietà di saturazione da calcolare
13) Per Pressione e Temperatura di saturazione andrà indicata la composizione molare e l'altra grandezza
14) Per la Composizione di Saturazione bisogna indicare T, p il numero di punti in cui dividere il range delle composizioni e il dT massimo fra Tsat calcolata e quella indicata
15) Per ogni specie chimica va indicato un valore minimo e uno massimo
16) IMPORTANTE: selezionare un fluido da utilizzare come complementare per far tornare la somma delle composizioni = 1 (consiglio utilizzare quella presente in maggior quantità)
