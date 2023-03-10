import sqlite3
from datetime import datetime

class Connessione:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS esercizi (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            nome TEXT (50) NOT NULL,
            numero_ripetizioni INTEGER NOT NULL,
            numero_serie INTEGER NOT NULL,
            riposo_minuti NUMERIC NOT NULL,
            giorno DATE NOT NULL,
            gruppo_muscolare INTEGER REFERENCES [gruppo_muscolare] (id) ON DELETE SET NULL ON UPDATE SET NULL
            );
        """)
        self.conn.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gruppo_muscolare (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            nome TEXT (50) NOT NULL UNIQUE ON CONFLICT IGNORE
            );
        """)
        self.conn.commit()

        self.cursor.execute("""
            INSERT OR IGNORE INTO gruppo_muscolare(nome)
            VALUES
                ("Pettorali"),
                ("Addominali"),
                ("Bicipiti"),
                ("Deltoidi"),
                ("Tricipiti"),
                ("Dorsali"),
                ("Trapezi"),
                ("Quadricipiti"),
                ("Polpacci");
        """)
        self.conn.commit()

    def insert(self,
                nome: str,
                numero_ripetizioni: int,
                numero_serie: int,
                riposo_minuti: float,
                giorno: datetime,
                gruppo_muscolare: int):
        self.cursor.execute("""
            INSERT INTO esercizi(nome, numero_ripetizioni, numero_serie, riposo_minuti, giorno, gruppo_muscolare)
            VALUES(?,?,?,?,?,?);
            """, (nome, numero_ripetizioni, numero_serie, riposo_minuti, giorno, gruppo_muscolare))
        self.conn.commit()

    def display(self):
        self.cursor.execute("""
            SELECT 
                giorno,
                esercizi.nome, 
                gruppo_muscolare.nome AS gruppo_muscolare,
                numero_ripetizioni, 
                numero_serie, 
                riposo_minuti, 
                esercizi.id
            FROM esercizi
            INNER JOIN gruppo_muscolare
            ON gruppo_muscolare.id = esercizi.gruppo_muscolare
            ORDER BY giorno ASC;
            """)
        return self.cursor.fetchall()

    def tab_gruppi_musc(self):
        self.cursor.execute("""
            SELECT id, nome
            FROM gruppo_muscolare
            """)
        return self.cursor.fetchall()

    def cancella(self, id: int):
        # eliminare un esercizio in base all'id
        self.cursor.execute("""
            DELETE 
            FROM esercizi 
            WHERE id=?;
            """, (id,))
        self.conn.commit()
