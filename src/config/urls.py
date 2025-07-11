# src/config/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from expense_tracker.core import views

router = DefaultRouter()
# Register the ExpenseViewSet with the router
router.register(r'expenses', views.ExpenseViewSet, basename='expense')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # Include the router's URLs under the 'api/' path
    path('api/', include(router.urls)),
]