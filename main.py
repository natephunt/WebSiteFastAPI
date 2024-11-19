from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel 

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)

@app.get('/styles.css')
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("styles.css", context)

@app.get("/button", response_class=HTMLResponse)
def get(request: Request) -> str:
    context = {'request': request}
    return templates.TemplateResponse("button.html", context)

@app.get('/replace', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("replace.html", context)