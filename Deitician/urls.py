from django.urls import path
from .views import DietSuggestion

urlpatterns = [
    path('suggestion/', DietSuggestion.as_view())
]
