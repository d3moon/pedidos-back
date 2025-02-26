from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from uuid import uuid4
from datetime import datetime

Base = declarative_base()

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    cliente = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    descricao = Column(String(255))
