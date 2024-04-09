from shared.database import Base
from sqlalchemy import Column, Integer, String, Numeric


class ContaPagarReceber(Base):
    __tablename__ = "contas_a_pagar_e_receber"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)
    valor = Column(Numeric,nullable=False)
    tipo = Column(String, nullable=False)