# src/config/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from expense_tracker.core import views

router = DefaultRouter()
router.register(r'expenses', views.ExpenseViewSet, basename='expense') # Register the ExpenseViewSet with the router

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),     # Include the router's URLs under the 'api/' path
]