# app/models/user.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    """
    Represents a user in the system, who can have expenses, budgets, categories, alerts, notifications,
    and can participate in groups for shared expense tracking.
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Relationships
    expenses = relationship("Expense", back_populates="owner", cascade="all, delete-orphan")
    budgets = relationship("Budget", back_populates="owner", cascade="all, delete-orphan")
    categories = relationship("Category", back_populates="owner", cascade="all, delete-orphan")
    alerts = relationship("Alert", back_populates="owner", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="owner", cascade="all, delete-orphan")
    group_members = relationship("GroupMember", back_populates="user", cascade="all, delete-orphan")
    group_expenses = relationship("GroupExpense", back_populates="user", cascade="all, delete-orphan")
    expense_splits = relationship("ExpenseSplit", back_populates="user", cascade="all, delete-orphan")
