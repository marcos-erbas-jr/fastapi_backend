from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app_blx.db" #url com o nome do banco
                                                # alterado para app_blx.db
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#acima é a comunicação com o banco de dados

Base = declarative_base()
#Classe Base instaciada para herdar os modelos, permitindo que as classes
#possam ir e vir no banco de dados

#Importações e código acima retirados da documentação do FastAPI

def criar_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()