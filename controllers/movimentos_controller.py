from sqlalchemy.orm import Session
from models.movimentos import Movimentos

def create_movimento(db: Session, movimento_data: dict):
  db_movimento = Movimentos(
      id_caixa=movimento_data['id_caixa'],
      tipo_movimento=movimento_data['tipo_movimento'],
      valor=movimento_data['valor'],
      data_hora=movimento_data['data_hora'],
      descricao=movimento_data['descricao']
  )
  db.add(db_movimento)
  db.commit()
  db.refresh(db_movimento)
  return db_movimento

def get_movimentos(db: Session):
  return db.query(Movimentos).all()