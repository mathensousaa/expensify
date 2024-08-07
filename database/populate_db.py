from sqlalchemy.orm import Session
from models.user import User
from models.expense import Expense


def populate_db(db: Session):
    # Adicionar usuários fictícios
    user1 = User(
        first_name="John",
        last_name="Doe",
        birth_date="1990-01-01",
        username="johndoe",
        email="john.doe@example.com",
        phone_number="1234567890",
        hashed_password="hashedpassword1",
    )

    user2 = User(
        first_name="Jane",
        last_name="Smith",
        birth_date="1985-05-05",
        username="janesmith",
        email="jane.smith@example.com",
        phone_number="0987654321",
        hashed_password="hashedpassword2",
    )

    db.add(user1)
    db.add(user2)
    db.commit()

    # Adicionar despesas fictícias
    expense1 = Expense(
        description="Lunch", amount=15.00, date="2024-08-06", user_id=user1.id
    )

    expense2 = Expense(
        description="Groceries", amount=45.50, date="2024-08-06", user_id=user1.id
    )

    expense3 = Expense(
        description="Rent", amount=500.00, date="2024-08-01", user_id=user2.id
    )

    db.add(expense1)
    db.add(expense2)
    db.add(expense3)
    db.commit()

    print("Banco de dados populado com dados fictícios.")
