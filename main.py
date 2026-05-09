from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Asegúrate de que la carpeta 'static' exista en tu proyecto
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

ARTISTAS_DB = {
    "jose_jose": {
        "nombre": "José José",
        "foto": "jose_jose.jpg",
        "descripcion": "José José, el 'Príncipe de la Canción', fue un ícono de la balada romántica..."
    },
    "luis_miguel": {
        "nombre": "Luis Miguel",
        "foto": "luis_miguel.webp",
        "descripcion": "Luis Miguel, apodado 'El Sol de México', es uno de los artistas más exitosos..."
    },
    "camilo_sesto": {
        "nombre": "Camilo Sesto",
        "foto": "camilo_sesto.jpg",
        "descripcion": "Camilo Sesto fue uno de los cantantes y compositores más completos..."
    }
}

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    # CORRECCIÓN: Usamos argumentos nombrados (request=request)
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )

@app.get("/perfil/{artista_id}", response_class=HTMLResponse)
async def read_artista(request: Request, artista_id: str):
    datos = ARTISTAS_DB.get(artista_id)
    if not datos:
        return HTMLResponse(content="Artista no encontrado", status_code=404)
    
    # CORRECCIÓN: Pasamos el contexto de forma explícita
    return templates.TemplateResponse(
        request=request, 
        name="artistas.html", 
        context={
            "nombre": datos["nombre"],
            "foto": datos["foto"],
            "descripcion": datos["descripcion"]
        }
    )