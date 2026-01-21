from pydantic import BaseModel
from typing import List, Optional

# 1. Modello Dati (Schema)
class Panino(BaseModel):
    id: int
    nome: str
    descrizione: str
    prezzo: float
    ingredienti: str  # Es: "Pane nero, Carne di Drago, Lattuga"

# 2. Simulazione Database in memoria
# Iniziamo con qualche panino pre-caricato
db_panini: List[Panino] = [
    Panino(id=1, nome="Il Drago Fiammante", descrizione="Piccantissimo con salsa lavica", prezzo=12.50, ingredienti="Pane Rosso, Jalapeno, Carne, Tabasco"),
    Panino(id=2, nome="Elfo Vegano", descrizione="Leggero come una piuma", prezzo=9.00, ingredienti="Pane Integrale, Hummus, Rucola, Pomodori"),
]

def get_all_panini():
    return db_panini

def add_panino(nome, descrizione, prezzo, ingredienti):
    # Genera un ID progressivo
    new_id = db_panini[-1].id + 1 if db_panini else 1
    new_panino = Panino(id=new_id, nome=nome, descrizione=descrizione, prezzo=prezzo, ingredienti=ingredienti)
    db_panini.append(new_panino)

def delete_panino(panino_id: int):
    global db_panini
    # Filtra la lista mantenendo solo i panini che NON hanno quell'ID
    db_panini = [p for p in db_panini if p.id != panino_id]