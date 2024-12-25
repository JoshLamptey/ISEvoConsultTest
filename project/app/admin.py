from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Client,Domain

# Register your models here for admin support
admin.site.register(Domain)
#client model
admin.site.register(Client)
