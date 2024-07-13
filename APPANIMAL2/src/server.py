from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #Importando o CORS Middleware
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4 #Biblioteca uuid para gerar códigos de número
                        #como se fosse hash

app = FastAPI()

#Configuração do CORS - Permitir requisições de origens diferentes
''''Como o front e back estão hospedados em portas diferente, torna-se necessário'
configurar o CORS, onde adicionamos as origens que são permitidas fazer 
requisições em uma lista chamada origins, depois configuramos o middleware

Conceito de Middleware:
O middleware é o software que se encontra entre o servidor e os 
aplicativos(clientes) nele executados. Essencialmente, o middleware funciona 
como uma camada oculta de tradução, permitindo a comunicação e o gerenciamento 
de dados para aplicativos distribuídos.'''
origins = ["http://localhost:63342"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel): #Classe Animal herdou o BaseModel de pydantic
    id: Optional[int] = None #Id agora é opcional, Pois receberá um código
    nome: str                # gerado por uuid4()
    idade: int
    sexo: str
    cor:str

banco: List[Animal] = [] #banco está tipado com uma lista com classe Animal

@app.get('/')
def home():
    return{'msg': 'API Funcionando'}

@app.get('/animais')
def listar_animais():
    return banco

@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return {'msg': f'{animal.nome} foi encontrado no Banco de Dados'}
    return {'erro': 'Animal não localizado'}

@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            nome = animal.nome
            banco.remove(animal)
            return {'msg': f'{nome} foi removido'}
    return {'erro': 'Animal não localizado'}

@app.post('/animais')
def criar_animais(animal: Animal):
    animal.id = str(uuid4()) #id receberá um código, para animal.id não
                            #receber um Objeto uuid, ele é convertido
                            # antes para string
    banco.append(animal)
    return None #Não retorna nada