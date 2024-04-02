# Create your models here.
from django.db import models


class AccountType(models.Model):
    CLIENT = 'Client'
    PARTNER = 'Partner'
    TYPE_CHOICES = (
        (CLIENT, 'Client'),
        (PARTNER, 'Partner'),
    )
    name = models.CharField(max_length=255, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.pk} {self.name}"


class AccountStatus(models.Model):
    IMPLEMENTATION = 'Implementation'
    ACTIVE = 'Active'
    DEACTIVATED = 'Deactivated'
    STATUS_CHOICES = (
        (IMPLEMENTATION, 'Implementation'),
        (ACTIVE, 'Active'),
        (DEACTIVATED, 'Deactivated'),
    )
    name = models.CharField(max_length=255, choices=STATUS_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} {self.name}"


class Account(models.Model):
    WEEKLY = 'weekly'
    BIWEEKLY = 'bi-weekly'
    UNKNOWN = 'unknown'
    PAYROLL_FREQ_CHOICES = (
        (WEEKLY, 'WEEKLY'),
        (BIWEEKLY, 'BIWEEKLY'),
        (UNKNOWN, 'UNKNOWN'),
    )
    API = 'API'
    SFTP = 'SFTP'
    PAYROLL_RECEIVE_CHOICES = (
        (API, 'API'),
        (SFTP, 'SFTP'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500)
    payroll_frequency = models.CharField(max_length=100, choices=PAYROLL_FREQ_CHOICES)
    payroll_receive_method = models.CharField(max_length=100, choices=PAYROLL_RECEIVE_CHOICES)
    account_type = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    account_status = models.ForeignKey(AccountStatus, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PartnerAccount(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    partnership_started = models.DateField()

    def __str__(self):
        return f"{self.account.name} - {self.partner.name}"


class Payroll(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    check_date = models.DateField()
    pay_start = models.DateField()
    pay_end = models.DateField()
    gross_hours = models.DecimalField(
        max_digits=10, decimal_places=2,
        blank=True, null=True
    )
    base_wages = models.DecimalField(
        max_digits=20, decimal_places=2,
        blank=True, null=True
    )
    overtime_wages = models.DecimalField(
        max_digits=20, decimal_places=2,
        default=0, blank=True, null=True
    )
    other_wages = models.DecimalField(
        max_digits=20, decimal_places=2,
        default=0, blank=True, null=True
    )
    gross_wages = models.DecimalField(
        max_digits=20, decimal_places=2,
        default=0, blank=True, null=True
    )
    bonus_wages = models.DecimalField(
        max_digits=20, decimal_places=2,
        default=0, blank=True, null=True
    )
    commission_wages = models.DecimalField(
        max_digits=20, decimal_places=2,
        blank=True, null=True
    )
    incentive_wages = models.DecimalField(
        max_digits=20, decimal_places=2,
        blank=True, null=True
    )
    custom_wages = models.JSONField(
        default=dict, help_text='Additional non-standard wages'
    )
