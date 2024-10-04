from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class OpCredito(Base):
  __tablename__ = "op_creditos"
  id = Column(Integer, primary_key=True, index=True)
  id_caixa = Column(Integer, ForeignKey('caixas.id'))
  id_operadora = Column(Integer, ForeignKey('operadoras_credito.id'))
  data_extrato = Column(Date)
  total_credito = Column(Float)
  total_debito = Column(Float)
  valor_pix = Column(Float, default=0)
  valor_voucher = Column(Float, default=0)
  caixa = relationship("Caixa", back_populates="op_credito")
  operadora = relationship("OperadoraCredito", back_populates="op_credito")