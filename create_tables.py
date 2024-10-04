from sqlalchemy import create_engine
from models.base import Base
from models.caixa import Caixa
from models.operadora_credito import OperadoraCredito
from models.op_credito import OpCredito
from models.movimentos import Movimentos

DATABASE_URL = "sqlite:///finance.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    create_tables()