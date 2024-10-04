from sqlalchemy.orm import Session
from models.caixa import Caixa

def create_caixa(db: Session, caixa_data: dict):
  fechamento_do_caixa = (
      caixa_data['saldo_inicial'] + caixa_data['valor_cartao_credito'] +
      caixa_data['valor_cartao_debito'] + caixa_data['valor_ifood'] +
      caixa_data['valor_dinheiro'] + caixa_data['valor_fiado'] +
      caixa_data['valor_acrescimo'] - caixa_data['saidas_caixa']
  )
  db_caixa = Caixa(
      caixa_aberto=caixa_data['caixa_aberto'],
      data=caixa_data['data'],
      saldo_inicial=caixa_data['saldo_inicial'],
      valor_cartao_credito=caixa_data['valor_cartao_credito'],
      valor_cartao_debito=caixa_data['valor_cartao_debito'],
      valor_ifood=caixa_data['valor_ifood'],
      valor_dinheiro=caixa_data['valor_dinheiro'],
      valor_fiado=caixa_data['valor_fiado'],
      saidas_caixa=caixa_data['saidas_caixa'],
      valor_acrescimo=caixa_data['valor_acrescimo'],
      fechamento_do_caixa=fechamento_do_caixa
  )
  db.add(db_caixa)
  db.commit()
  db.refresh(db_caixa)
  return db_caixa

def get_caixas(db: Session):
  return db.query(Caixa).all()