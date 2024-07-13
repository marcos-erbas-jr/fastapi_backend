from fastapi import FastAPI
from pydantic import BaseModel #Aula 6 - Modelo usado no request

app = FastAPI()
'''
@app.get('/') 
O Decorator ('@' arroba) é uma feature que permite modificar ou aprimorar o 
comportamento de funções, métodos ou classes.

Depois temos o método get que é um dos métodos http. 
É usado para obter algum recurso hospedado no servidor.

Por último temos o ('/') que é o path (caminho, rota, route ou endpoint)

Ou seja, quando o endereço por exemplo for: http://127.0.0.1:8000/
chamará a função root() e mostrará {"messagem": "Hello World!"}
'''
@app.get('/')
async def root():
    return {"messagem": "Hello World!"}

# Comando usado para rodar o servidor desse código:
# uvicorn helloworld:app --reload  | Obs.: o helloworld é o nome do arquivo
#Obs.: No FastAPI pode ser usar o /docs, por exemplo:
# http://127.0.0.1:8000/docs   será mostrado a documentação com todas a
#rotas e seus métodos configurados

'''
Em aplicação REST, os métodos mais utilizados são:

O método GET é o método mais comum, geralmente é usado para solicitar que 
um servidor envie um recurso;

O método POST foi projetado para enviar dados de entrada para o servidor. 
Na prática, é frequentemente usado para suportar formulários HTML;

O método PUT edita e atualiza documentos em um servidor;

O método DELETE que como o próprio nome já diz, deleta certo dado ou coleção
do servidor.
'''
# é possível utilizar métodos diferentes para o mesmo path, note que todos
#são '/profile'
@app.get('/profile')
def profile():
    return {"nome": "Marcos"}

@app.post('/profile')
def profile():
    return {"messagem": "Criado novo perfil"}

@app.put('/profile')
def profile():
    return {"messagem": "Perfil atualizado"}

@app.delete('/profile')
def profile():
    return {"messagem": "Perfil deletado"}

#uso de parâmetro na rota
@app.get('/nickname/{nick}')
def nicknamen(nick):
    return{'mensagem': f'Olá, {nick}'}
#Ao digitar http://localhost:8000/nickname/Marcos terei como resposta:
# {"mensagem":"Olá, Marcos"} pois o 'Marcos' é o parâmetro nick
# solicitado na rota

@app.get('/potencia/{numero}')
def quadrado(numero:int): #O :int é usado para tipar no
# python como int, ao utilizar a tipagem, ocorrerá uma espécie
# de validação, qualquer coisa que não for um inteiro será
# rejeitado e retornará erro como:
#request: http://localhost:8000/potencia/coisa
# {"detail":[{"type":"int_parsing","loc":["path","numero"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"coisa"}]}
    square = numero * numero
    text = f"O quadrado de {numero} é {square}"
    return text

# >>Query String, geralmente aparece no url como:
# http:localhost/path?value=valor passado, sendo 'value' o nome
# do parâmetro
@app.get('/dobro')
def dobro(valor:int):
    resultado = valor * 2
    return {'resultado': f'O dobro de {valor} é {resultado}'}
# http://localhost:8000/dobro?valor=2 ,exemplo de url da rota acima
# Em resumo criamos uma rota normal, mas na função colocamos um
#parâmetro, e isso já é o suficiente para torna-se uma query string
# No exemplo anterior o parâmetro já aparece na própria rota
# @app.get('/potencia/{numero}'), na query string isso não é
# necessário

#Query String com mais de um parâmetro
@app.get('/area')
def area_retangulo(largura:int, comprimento:int):
    area = largura * comprimento
    return {'area': f'A area de um retângulo {largura}x{comprimento}'
                    f' é {area}'}
# Exemplo da url:
# http://localhost:8000/area?largura=10&comprimento=5
# Note que após o '?' os parâmetros são divididos por &
#resposta para url acima:
# {"area":"A area de um retângulo 10x5 é 50"}

# Query String com valor padrão
@app.get('/value')
def area_retangulo(value:int = 0):
    return {'value': f'{value}'}
# Nesse valo já definimos o value como sendo zero por padrão
# dessa forma a passagem de alguma valor para o parâmetro
# torna-se opcional
#Exemplo da url sem parâmetro:
#http://localhost:8000/value
# Resposta:
# {"value":"0"}

#Exemplo da url com parâmetro:
#http://localhost:8000/value?value=257
# Resposta:
# {"value":"257"}

#Request Body
class Produto(BaseModel):
    '''A classe Produto herda a classe BaseModel da biblioteca
    pydantic, pois esta que é utilizada pelo FastAPI, esse modelo
    será usado no Request Body'''
    name: str
    valor: float
    #Ambos foram tipados, para só aceitarem valores com os tipos definidos


@app.post('/produto')
def produtos(produto: Produto): #Exige um parâmetro 'produto' com tipo
    # da classe Produto
    return{"mensagem": f'Produto {produto.name}  Valor: R${produto.valor}'}

# O código 200 é quando uma Request foi enviada com sucesso

