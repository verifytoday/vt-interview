from django.contrib import admin
from .models import Account, Partner, PartnerAccount

admin.site.register(Account)
admin.site.register(Partner)
admin.site.register(PartnerAccount)
