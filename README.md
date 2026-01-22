# 🍔 FantaBurger - Gestionale 

**FantaBurger** è una Web Application dinamica sviluppata in Python con **FastAPI**.
Il progetto simula un sistema gestionale per una hamburgeria , permettendo di gestire un menu di panini e ingredienti.
In grado di aggiungere prezzo e una breve descrizione ad ogni panino.

L'applicazione implementa un'architettura **MVC** (Model-View-Controller) e operazioni **CRUD** complete.

## 👥 Il Team
* De Simone Tommaso
* Laudisio Andrea
* De gennaro Francesco 
* Petraccone Riccardo
* Casabona Giuseppe

## 🛠️ Stack Tecnologico
* **Backend:** Python 3.x, FastAPI, Uvicorn
* **Frontend:** HTML5, CSS3, Jinja2 Templates
* **Dati:** Struttura dati in memoria 

## 🚀 Installazione e Avvio

Per eseguire il progetto in locale, segui questi passaggi:

### 1. Clona la repository
```bash
git clone https://github.com/Tommrex/FantaBurger.git
cd FantaBurger
```

### 2. Crea e attiva l'ambiente virtuale 
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3.Installa le dipendenze
```bash
pip install -r requirements.txt
```
### 4.Avvia il Server
```bash
uvicorn app.main:app --reload
```
#### Una volta avviato, apri il browser:
* Menu Pubblico: http://127.0.0.1:8000
* Gestione Cucina (Admin): http://127.0.0.1:8000/admin

##### 📂 Struttura del Progetto
* /app: Contiene il codice sorgente (main, database).
* /app/templates: File HTML (Jinja2).
* /app/static: Fogli di stile CSS e assets.
