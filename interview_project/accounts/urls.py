# Inside your app's urls.py
from django.urls import path
from .views import active_accounts

urlpatterns = [
    path('active-accounts/', active_accounts, name='active-accounts'),
]
