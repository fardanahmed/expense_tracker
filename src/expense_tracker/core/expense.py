# src/expense_tracker/core/expense.py
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Expense:
    """Represents a single financial expense."""
    amount: float
    category: str
    description: str
    expense_date: date

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount must be non-negative")