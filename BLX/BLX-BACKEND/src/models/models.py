from pydantic import BaseModel
from typing import Optional, List
class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str

class Produto(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    #meus_produtos: List[Produto] = Produto
    minhas_vendas: List[str]
    meus_pedidos: List[str]
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
