from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# special_argument = '%40' # at = @

SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:123456@localhost:5432/contas_a_pagar_e_contas_a_receber'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
