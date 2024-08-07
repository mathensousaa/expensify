from models.expense import Expense
from database.db_session import SessionLocal


def add_expense(description, amount, date, user_id):
    db = SessionLocal()
    expense = Expense(
        description=description, amount=amount, date=date, user_id=user_id
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    db.close()
    return expense


def get_expenses_by_date(date, user_id):
    db = SessionLocal()
    expenses = (
        db.query(Expense).filter(Expense.date == date, Expense.user_id == user_id).all()
    )
    db.close()
    return expenses


def update_expense(expense_id, user_id, description=None, amount=None, date=None):
    db = SessionLocal()
    expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id, Expense.user_id == user_id)
        .first()
    )
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


def delete_expense(expense_id, user_id):
    db = SessionLocal()
    expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id, Expense.user_id == user_id)
        .first()
    )
    if not expense:
        return None

    db.delete(expense)
    db.commit()
    db.close()
    return expense_id


def get_all_expenses(user_id):
    db = SessionLocal()
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    db.close()
    return expenses
