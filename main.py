from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

db=[]

class city(BaseModel):
    name : str 
    timezone :str

@app.get('/')
def index():
    return{'key':'value'}

@app.get('/cities')
def get_cities():
    return db

# @app.get('/cities/{city_id}')

# @app.get('/cities')
# def create_city(city)


# @app.delete('/cities')