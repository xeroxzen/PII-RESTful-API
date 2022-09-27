from django.contrib import admin
from .models import Pii

@admin.register(Pii)
class PiiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address', 'ssn', 'dob', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone', 'address', 'ssn', 'dob')
    list_per_page = 25

