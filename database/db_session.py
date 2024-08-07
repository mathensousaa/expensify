from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///expensify.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    import models.expense
    import models.user
    from .populate_db import populate_db

    Base.metadata.create_all(bind=engine)

    # Populando o banco de dados com dados fictícios
    db = SessionLocal()
    # populate_db(db)
    db.close()
