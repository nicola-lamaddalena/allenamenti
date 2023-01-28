# allenamenti - workout app
Web app creata per tenere traccia di allenamenti fisici.

Scritta in Python usando Flask e SQLite3 per il backend e semplice HTML, CSS e JS per il frontend con l'uso dei template di Jinja2.

## Introduzione
L'obiettivo di questa app è tenere traccia dei miei allenamenti senza usare programmi come Microsoft Excel o Google Sheets. È stata anche un'occasione per imparare il framework Flask.

## Tecnologie usate
- Python 3.10.2
- Flask 2.2.2
- Jinja 3.1.2

## Setup
Per lanciare questa app, attivare prima l'ambiente virtuale:
```
> cd \projectDir
> venv\Scripts\activate
```
Questi comandi funzionano su Windows.

## Avvio
L'app può essere avviata in due modi: normale o debug (nel caso in cui vogliate cambiarne degli aspetti senza dover riavviare ogni volta il server).
- Modalità normale
```
> flask --app app run
```
- Modalità debug
```
> flask --app app --debug run
```

## Utilizzo 
L'app da la possibilità di aggiungere gli allenamenti, visualizzarli in una tabella e rimuoverli fornendo l'id associato.
Ci sono dei gruppi muscolari pre-inseriti, visualizzabili cliccando nell'input specifico. Possono essere modificati nella tabella "gruppo_muscolare" presente nel database.
![tab_grp_musc](.\images\tab_gruppi_muscolari.png).


