import os
import socket
import uuid
from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def hello_world():
    return {'message': 'hello world'}

@app.get('/hostname')
def get_hostname():
    return {'hostname': socket.gethostname()}

@app.get('/author')
def get_author():
    return {'author': os.environ.get('AUTHOR')}

@app.get('/id')
def get_id():
    os.environ['UUID'] = str(uuid.uuid4())
    return {'UUID': os.environ.get('UUID')}
