from django.contrib import admin

# Register your models here.
from apps.address.models import Address

admin.site.register(Address)
