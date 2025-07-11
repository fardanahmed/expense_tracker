# src/expense_tracker/core/serializers.py
from rest_framework import serializers
from.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id',
            'amount',
            'category',
            'description',
            'expense_date',
            'created_at',
            'updated_at'
        ]