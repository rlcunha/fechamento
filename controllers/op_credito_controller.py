from sqlalchemy.orm import Session
from models.op_credito import OpCredito

def create_op_credito(db: Session, op_credito_data: dict):
  db_op_credito = OpCredito(
      id_caixa=op_credito_data['id_caixa'],
      id_operadora=op_credito_data['id_operadora'],
      data_extrato=op_credito_data['data_extrato'],
      total_credito=op_credito_data['total_credito'],
      total_debito=op_credito_data['total_debito'],
      valor_pix=op_credito_data['valor_pix'],
      valor_voucher=op_credito_data['valor_voucher']
  )
  db.add(db_op_credito)
  db.commit()
  db.refresh(db_op_credito)
  return db_op_credito

def get_op_creditos(db: Session):
  return db.query(OpCredito).all()