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


def get_expenses_by_date(date):
    db = SessionLocal()
    expenses = db.query(Expense).filter(Expense.date == date).all()
    db.close()
    return expenses


def update_expense(expense_id, description=None, amount=None, date=None):
    db = SessionLocal()
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        return None

    if description:
        expense.description = description
    if amount:
        expense.amount = amount
    if date:
        expense.date = date

    db.commit()
    db.refresh(expense)
    db.close()
    return expense


def delete_expense(expense_id):
    db = SessionLocal()
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        return None

    db.delete(expense)
    db.commit()
    db.close()
    return expense_id


def get_all_expenses():
    db = SessionLocal()
    expenses = db.query(Expense).all()
    db.close()
    return expenses
