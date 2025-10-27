# pip install fastapi uvicorn jinja2 python-multipart

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates

# python -m uvicorn main:app --reload

app = FastAPI(title="Lista de alunos")


#Definir a pasta onde está os html
templetes = Jinja2Templates(directory="templetes")

#Definir a pasta onde os arquivos estaticos (CSS, Imagem e JS)
app.mount("/static",StaticFiles(directory="static"), name="static")
alunos = [
    {"nome": "Iago", "nota": 8.5},
    {"nome": "Murilo", "nota": 6.5},
    {"nome": "Joana", "nota" : 9.5},
    {"nome": "Francisco", "nota": 8.0}
]




#Rota inicial
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templetes.TemplateResponse(
        "index.html",
        {"request": request, "lista_alunos": alunos}
    )

@app.get("/cadastro", response_class=HTMLResponse)
def tela_cadastro(request: Request):
    return templetes.TemplateResponse(
        "cadastro.html",
        {"request": request}
    )
@app.post("/cadastro")
def salvar_aluno(nome: str = Form(...), nota: float = Form(...)):
    alunos.append({"nome": nome, "nota": nota})
    return RedirectResponse(url="/", status_code=303)

