from django.urls import path
from .views import display_forms
urlpatterns = [
    path('', display_forms)
]