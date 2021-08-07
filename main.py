from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Welcome to our main page!'

@app.get('/collegues')
def collegues():
    return 'Saya, Alina, Boris'

@app.get('/collegues/{name}')
def data_for_collegues(name):
    db_info = {
        'saya': {
            'sex': 'female',
            'position': 'accountant',
            'salary': 77000
        },
        'alina': {
            'sex': 'female',
            'position': 'software engineer',
            'salary': 95000
        },
        'boris': {
            'sex': 'male',
            'position': 'commercial manager',
            'salary': 95000
        }
    }
    if name in db_info:
       result = db_info[name]
    else:
       result = 'No information available'

    return result

import requests

@app.get('/collegues/{name}/jokes')
def jokes():
    url = 'https://official-joke-api.appspot.com/jokes/random'
    response = requests.get(url).json()

    return response['setup'], response['punchline']












