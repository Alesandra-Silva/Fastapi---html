# pip install fastapi uvicorn jinja2 python-multipart

from fastapi import FastAPi, Requests, RedirectResponse
from fastapi.response import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templetes

app = FastAPi(title="Lista de alunos")


#Definir a pasta onde está os html
templetes = Jinja2Templetes(directory="templetes")

#Definir a pasta onde os arquivos estaticos (CSS, Imagem e JS)
app.mount("/static",StaticFiles(directory="static"), name="static")
alunos = [
    {"nome": "Iago", "nota": 8.5}
    {"nome": "Murilo", "nota" 6.5}
    {"nome": "joana", "nota" 9.5}
    {"nome": "Francisco", "nota" 8.0}
]

#Rota inicial
@app.get("/", response_class=HTMLResponse)
def home(requests : Requests):
    return templetes.Templetesresponse(
        "index.html",
        {"requests": requests, "lista_alunos": alunos}
    )