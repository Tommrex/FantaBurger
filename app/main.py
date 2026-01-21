from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import get_all_panini, add_panino, delete_panino

app = FastAPI(title="FantaBurger 🍔")

# Configurazione file statici (CSS) e Template (HTML)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# --- ROTTE (ROUTES) ---

# 1. READ: Homepage (Menu Pubblico)
@app.get("/")
def read_root(request: Request):
    panini = get_all_panini()
    return templates.TemplateResponse("index.html", {"request": request, "panini": panini})

# 2. READ: Dashboard (Area Amministrativa)
@app.get("/admin")
def admin_panel(request: Request):
    panini = get_all_panini()
    return templates.TemplateResponse("dashboard.html", {"request": request, "panini": panini})

# 3. CREATE: Aggiungi un nuovo panino
@app.post("/add")
def create_panino(
    nome: str = Form(...),
    descrizione: str = Form(...),
    prezzo: float = Form(...),
    ingredienti: str = Form(...)
):
    add_panino(nome, descrizione, prezzo, ingredienti)
    return RedirectResponse(url="/admin", status_code=303)

# 4. DELETE: Cancella un panino
@app.get("/delete/{panino_id}")
def remove_panino(panino_id: int):
    delete_panino(panino_id)
    return RedirectResponse(url="/admin", status_code=303)