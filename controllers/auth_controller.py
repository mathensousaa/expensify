import flet as ft
from models.user import User
from database.db_session import SessionLocal
from session.session_manager import SessionManager
import bcrypt
from sqlalchemy.exc import SQLAlchemyError


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


def authenticate_user(page: ft.Page, identifier, password):
    db = SessionLocal()

    try:
        user = (
            db.query(User)
            .filter(
                (User.email == identifier)
                | (User.username == identifier)
                | (User.phone_number == identifier)
            )
            .first()
        )

        if user and verify_password(password, user.hashed_password):
            SessionManager.set_session(page, user.id, user.username)
            session = SessionManager.get_session(page)
            return {
                "success": True,
                "message": "Logado com sucesso",
                "session": session,
            }
        else:
            return {"success": False, "message": "Credenciais inválidas"}

    except SQLAlchemyError as e:
        return {"success": False, "message": f"Erro do banco de dados: {str(e)}"}

    finally:
        db.close()
