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