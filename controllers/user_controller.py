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

def get_user_by_id(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user

def update_user(user_id, username=None, email=None, hashed_password=None):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    if username:
        user.username = username
    if email:
        user.email = email
    if hashed_password:
        user.hashed_password = hashed_password
    
    db.commit()
    db.refresh(user)
    db.close()
    return user

def delete_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    db.delete(user)
    db.commit()
    db.close()
    return user_id

def get_all_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def get_user_by_email(email):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()
    return user
