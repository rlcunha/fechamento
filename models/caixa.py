from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Caixa(Base):
  __tablename__ = "caixas"
  id = Column(Integer, primary_key=True, index=True)
  caixa_aberto = Column(String, unique=True)
  data = Column(Date)
  saldo_inicial = Column(Float)
  valor_cartao_credito = Column(Float, default=0)
  valor_cartao_debito = Column(Float, default=0)
  valor_ifood = Column(Float, default=0)
  valor_dinheiro = Column(Float)
  valor_fiado = Column(Float, default=0)
  saidas_caixa = Column(Float)
  valor_acrescimo = Column(Float, default=0)
  fechamento_do_caixa = Column(Float, default=0)
  movimentos = relationship("Movimentos", back_populates="caixa")
  op_credito = relationship("OpCredito", back_populates="caixa")