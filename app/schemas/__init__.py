# app/schemas/__init__.py

from .auth import UserCreate, UserLogin, UserResponse, AdminCreate  # Auth-related schemas
from .expenses import ExpenseCreate, ExpenseResponse  # Expense-related schemas
from .categories import CategoryCreate, CategoryResponse  # Category-related schemas
from .budget import BudgetCreate, BudgetResponse  # Budget-related schemas
from .alerts import AlertResponse, AlertUpdate, AlertCreate
from .groups import Groups, GroupCreate, GroupExpenses, GroupExpenseCreate, GroupMembers, GroupMemberCreate, GroupMemberStatus, ExpenseSplits, ExpenseSplitCreate
from .notifications import NotificationResponse
from .debt_notifications import DebtNotifications, DebtNotificationCreate, DebtNotificationStatus
