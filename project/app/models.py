from django.db import models
from django_tenants.models import TenantMixin,DomainMixin

# Create your models here.
class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    company_description = models.CharField(max_length=500)
    address = models.CharField(max_length=50)


class Domain(DomainMixin):
    pass 