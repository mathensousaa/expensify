from sqlalchemy import Column, Integer, String, Float, Date
from models import Base


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
