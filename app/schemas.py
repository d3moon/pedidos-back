from pydantic import BaseModel
from datetime import datetime

class PedidoCreate(BaseModel):
    cliente: str
    valor: float
    descricao: str = None

class PedidoResponse(PedidoCreate):
    id: str
    data_criacao: datetime

class IndicadorResponse(BaseModel):
    media_pedidos_por_cliente: float
