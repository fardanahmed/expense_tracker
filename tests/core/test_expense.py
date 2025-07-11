# tests/core/test_expense.py
import pytest
from datetime import date
from expense_tracker.core.expense import Expense # type: ignore

def test_create_expense_object():
    """
    GIVEN: Valid attributes for a new expense
    WHEN: An Expense object is created
    THEN: The object's attributes match the provided values
    """
    # Arrange
    expense_date = date(2024, 7, 26)

    # Act
    expense = Expense(
        amount=50.0,
        category="Food",
        description="Lunch with colleagues",
        expense_date=expense_date
    )

def test_create_expense_with_negative_amount_raises_error():
    """
    GIVEN: A negative amount for an expense
    WHEN: An attempt is made to create the Expense object
    THEN: A ValueError should be raised
    """
    with pytest.raises(ValueError, match="Amount must be non-negative"):
        Expense(
            amount=-10.0,
            category="Invalid",
            description="This should not be allowed",
            expense_date=date(2024, 1, 1)
        )

    # Assert
    assert expense.amount == 50.0
    assert expense.category == "Food"
    assert expense.description == "Lunch with colleagues"
    assert expense.expense_date == expense_date