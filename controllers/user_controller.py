from models.user import User
from database.db_session import SessionLocal


def create_user(username, email, hashed_password):
    db = SessionLocal()
    user = User(username=username, email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user
