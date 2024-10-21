from typing import Annotated
from fastapi import FastAPI, Form, Request
from pydantic import BaseModel

"""
сслыка на тестовое задание

https://docs.google.com/document/d/1WtMrIstCOd-ukMSTakjmIl7zCF6Px5S8p2txGsWb0vA/edit?tab=t.0
"""

#иницилизаяция приложение
app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str
    
## роутинги
@app.get("/")
def home_page():
    return {"Hello": "World"}
