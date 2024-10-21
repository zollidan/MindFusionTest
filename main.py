from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

"""
сслыка на тестовое задание

https://docs.google.com/document/d/1WtMrIstCOd-ukMSTakjmIl7zCF6Px5S8p2txGsWb0vA/edit?tab=t.0
"""

#иницилизаяция приложение
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


## роутинги
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/admin", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="admin.html"
    )