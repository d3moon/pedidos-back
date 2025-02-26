from sqlalchemy.orm import Session
import models
import schemas

def criar_pedido(db: Session, pedido: schemas.PedidoCreate):
    db_pedido = models.Pedido(**pedido.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

def listar_pedidos(db: Session):
    return db.query(models.Pedido).all()

def obter_pedido(db: Session, pedido_id: str):
    return db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()

def atualizar_pedido(db: Session, pedido_id: str, pedido_update: schemas.PedidoCreate):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()
    for key, value in pedido_update.dict(exclude_unset=True).items():
        setattr(db_pedido, key, value)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

def remover_pedido(db: Session, pedido_id: str):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()
    db.delete(db_pedido)
    db.commit()

def indicador(db: Session):
    total_pedidos = db.query(models.Pedido).count()
    total_clientes = db.query(models.Pedido.cliente).distinct().count()
    media_pedidos = total_pedidos / total_clientes if total_clientes > 0 else 0
    return {"media_pedidos_por_cliente": media_pedidos}
