from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Account


def active_accounts(request):
    """
    Collect and return active accounts, their payroll, and partners.
    """
    accounts = None
    payroll = None
    partners = None

    # ...

    return render(
        request,
        'active_accounts.html',
        {
            'accounts': accounts,
            'payroll': payroll,
            'partners': partners,
        }
    )
