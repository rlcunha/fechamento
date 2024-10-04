from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class OperadoraCredito(Base):
    __tablename__ = "operadoras_credito"
    id = Column(Integer, primary_key=True, index=True)
    nome_operadora = Column(String, unique=True)
    op_credito = relationship("OpCredito", back_populates="operadora")