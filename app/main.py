from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import crud
import models
import schemas
import database

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/pedidos", response_model=schemas.PedidoResponse)
def criar_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    return crud.criar_pedido(db=db, pedido=pedido)

@app.get("/pedidos", response_model=list[schemas.PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return crud.listar_pedidos(db=db)

@app.get("/pedidos/{id}", response_model=schemas.PedidoResponse)
def obter_pedido(id: str, db: Session = Depends(get_db)):
    pedido = crud.obter_pedido(db=db, pedido_id=id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@app.put("/pedidos/{id}", response_model=schemas.PedidoResponse)
def atualizar_pedido(id: str, pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    pedido_atualizado = crud.atualizar_pedido(db=db, pedido_id=id, pedido_update=pedido)
    if pedido_atualizado is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido_atualizado

@app.delete("/pedidos/{id}")
def remover_pedido(id: str, db: Session = Depends(get_db)):
    crud.remover_pedido(db=db, pedido_id=id)
    return {"message": "Pedido removido com sucesso!"}

@app.get("/indicador", response_model=schemas.IndicadorResponse)
def indicador(db: Session = Depends(get_db)):
    return crud.indicador(db=db)
