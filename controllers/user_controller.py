from models.user import User
from database.db_session import SessionLocal
import bcrypt
from datetime import datetime
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


def create_user(
    first_name, last_name, birth_date, username, email, phone_number, password
):
    db = SessionLocal()

    try:
        # Converta birth_date de string para objeto date
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

        hashed_password = hash_password(password)
        user = User(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            username=username,
            email=email,
            phone_number=phone_number,
            hashed_password=hashed_password,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"success": True, "user": user}

    except IntegrityError as e:
        db.rollback()
        if "UNIQUE constraint failed: users.username" in str(e):
            return {
                "success": False,
                "error": "Nome de usuário já existe",
                "field": "username",
            }
        if "UNIQUE constraint failed: users.email" in str(e):
            return {"success": False, "error": "Email já existe", "field": "email"}
        if "UNIQUE constraint failed: users.phone_number" in str(e):
            return {
                "success": False,
                "error": "Número de telefone já existe",
                "field": "phone_number",
            }
        return {"success": False, "error": "Integrity error", "field": None}

    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "error": str(e)}

    finally:
        db.close()


def get_user_by_id(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user


def update_user(
    user_id,
    first_name=None,
    last_name=None,
    birth_date=None,
    username=None,
    email=None,
    phone_number=None,
    password=None,
):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if birth_date:
        user.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    if username:
        user.username = username
    if email:
        user.email = email
    if phone_number:
        user.phone_number = phone_number
    if password:
        user.hashed_password = hash_password(password)

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
