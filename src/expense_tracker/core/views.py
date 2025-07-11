# src/expense_tracker/core/views.py
from rest_framework import viewsets
from.models import Expense
from.serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows expenses to be viewed or edited.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer