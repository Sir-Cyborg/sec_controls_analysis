Security Controls Analysis

L'obiettivo è quello di associare delle keyword a ogni descrizione dei controlli di sicurezza.
Ci sono principalmente due strategie:
- 1. si confronta ogni descrizione dei controlli di sicurezza con un pool keyword predefinito (matching diretto)
- 2. estrazione automatica di un pool dato in input tutti i controlli di sicurezza

Il metodo 1 è piu preciso e definito in un contesto predefinito. Il metodo 2 puo scoprire nuovi contetti nascosti.


2 + 1 = Strategia ibrida
Estrazione di un pool iniziale proposto leggendo tutte le descizioni dei controlli, successivamente si scorre controllo per controllo confrontando la descrizione con il pool e facendo il match delle keyword trovate. Se il controllo specifico abbia altre parole rilevanti si aggiungono le parole nella lista dei match


FASE 1 - costruzione di un sistema che legga tutti i controlli e tiri fuori un pool proposto
FASE 2 - confronto controllo per controllo con un pool esistente e ne faccia il match delle parole trovate


FASE 1:
Le tecniche di classificazione usate in Keyword Extraction si dividono in 3 principali categorie:
- Statistical methods -> veloce ma superficiale
- Graph-based methods -> piu intelligenti, ma fancy
- Embedding-based / Deep Learning methods -> molto piu intelligenti, e molto piu fancy

metodo usato in questo progetto è Statistical methods, usando la tecnica RAKE (Rapid Automatic Keyword Extraction):
    Segmenta il testo in frasi candidate, calcola punteggio basato su: frequenza parole, posizione del testo

    Processo: Pre-processing, Candidatura di frasi possibili da considerare, scoring RAKE, selezione top-N in base al punteggio RAKE

    Risultati: MEH



-------------------
Keyword extraction basata su BERT (Bidirectional Encoder Representations from Transformers)  modello di deep learning sviluppato da Google. Produce embedding contestuali, cioè vettori che cambiano a seconda della frase in cui la parola compare. In pratica, le parole vengono rappresentati in vettori -> parole tipo "re" "regina" sono rappresentate vicine nello spazio -> piu acuratezza semantica.
 
 risultato: ['dati', 'firewall', 'utenti', 'vulnerabilità', 'complesse', 'password', 'conservate', 'protocolli', 'antivirus/edr', 'sicurezza', 'limitati', 'registrate', 'dispositivi', 'backup', 'autenticazione', 'aes-256', 'accesso', 'archiviate', 'privilegi', "l'accesso"]



