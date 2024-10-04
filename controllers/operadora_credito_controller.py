from sqlalchemy.orm import Session
from models.operadora_credito import OperadoraCredito

def create_operadora_credito(db: Session, nome_operadora: str):
  db_operadora = OperadoraCredito(nome_operadora=nome_operadora)
  db.add(db_operadora)
  db.commit()
  db.refresh(db_operadora)
  return db_operadora

def get_operadoras_credito(db: Session):
  return db.query(OperadoraCredito).all()