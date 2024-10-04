from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Movimentos(Base):
  __tablename__ = "movimentos"
  id = Column(Integer, primary_key=True, index=True)
  id_caixa = Column(Integer, ForeignKey('caixas.id'))
  tipo_movimento = Column(String)
  valor = Column(Float)
  data_hora = Column(Date)
  descricao = Column(String)
  caixa = relationship("Caixa", back_populates="movimentos")