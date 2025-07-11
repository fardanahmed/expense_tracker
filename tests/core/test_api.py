# tests/core/test_api.py
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from expense_tracker.core.models import Expense

@pytest.mark.django_db
def test_create_expense_api_endpoint():
    """
    GIVEN a DRF API client
    WHEN a POST request is sent to the /api/expenses/ endpoint with valid data
    THEN an expense should be created in the database and a 201 status returned.
    """
    client = APIClient()
    payload = {
        "amount": "99.50",
        "category": "Utilities",
        "description": "Monthly internet bill",
        "expense_date": "2024-08-01"
    }
    response = client.post("/api/expenses/", payload, format='json')

    # Assert the response is correct
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['category'] == "Utilities"

    # Assert the object was actually created in the database
    assert Expense.objects.count() == 1
    assert Expense.objects.get().amount == 99.50