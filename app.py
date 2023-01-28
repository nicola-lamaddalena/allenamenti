import os
from flask import Flask, render_template, request, redirect, url_for
from connessione import Connessione

DB = "fitness.db"
GRAFICI_DIR = os.path.join("static", "graficiAllenamenti")

app = Flask(__name__)
app.config["CARICA_DIR"] = GRAFICI_DIR

@app.route("/", methods=["GET", "POST"])
@app.route("/nuovoAllenamento", methods=["GET", "POST"])
def aggiungi_allenamento():
    conn = Connessione(DB)
    
    if request.method == "POST":
        esercizio = request.form.get("nome")
        ripetizioni = int(request.form.get("ripetizioni"))
        serie = int(request.form.get("serie"))
        riposo = float(request.form.get("riposo"))
        giorno = request.form.get("giorno")
        gruppo_musc = int(request.form.get("gruppo_musc"))
        conn.insert(esercizio, ripetizioni, serie, riposo, giorno, gruppo_musc)

    gruppi = conn.tab_gruppi_musc()
    return render_template("nuovoAllenamento.html", gruppi=gruppi)

@app.route("/visualizzaAllenamenti", methods=["GET", "POST"])
def visualizza_allenamenti():
    conn = Connessione(DB)
    dati = conn.display()

    if request.method == "POST":
        if request.form.get("elimina") == "Elimina esercizio":
            id_esercizio = request.form.get("elimina")
            conn.cancella(id_esercizio)
            dati = conn.display()

    return render_template('visualizzaAllenamenti.html', dati=dati)
