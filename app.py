import os
from flask import Flask, render_template, request, redirect, url_for
from connessione import Connessione
import matplotlib.pyplot as plt

DB = "fitness.db"
GRAFICI_DIR = os.path.join("static", "graficiAllenamenti")

app = Flask(__name__)
app.config["CARICA_DIR"] = GRAFICI_DIR


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        render_template("nuovoAllenamento.html")

    return render_template("index.html")

@app.route("/nuovoAllenamento", methods=["GET", "POST"])
def aggiungi_allenamento():
    if request.method == "POST":
        esercizio = request.form.get("nome")
        ripetizioni = int(request.form.get("ripetizioni"))
        serie = int(request.form.get("serie"))
        riposo = float(request.form.get("riposo"))
        giorno = request.form.get("giorno")
        gruppo_musc = int(request.form.get("gruppo_musc"))
        conn = Connessione(DB)
        conn.insert(esercizio, ripetizioni, serie, riposo, giorno, gruppo_musc)

    return render_template("nuovoAllenamento.html")

@app.route("/visualizzaAllenamenti")
def visualizza_allenamenti():
    conn = Connessione(DB)
    dati = conn.display()
    return render_template('visualizzaAllenamenti.html', dati=dati)

@app.route("/grafici")
def viz():
    full_filename = os.path.join(app.config["CARICA_DIR"], "grafici.png")
    conn = Connessione(DB)
    dati = conn.display()

    if "grafico.png" not in app.config["CARICA_DIR"]:
        plt.bar([dato[4] for dato in dati], [dato[1] for dato in dati])
        plt.savefig(full_filename)

    return render_template("grafici.html", grafico = full_filename)
