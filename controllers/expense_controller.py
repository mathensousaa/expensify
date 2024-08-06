from models.expense import Expense
from database.db_session import SessionLocal


def add_expense(description, amount, date):
    db = SessionLocal()
    expense = Expense(description=description, amount=amount, date=date)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    db.close()
    return expense
