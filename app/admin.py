from django.contrib import admin

from app.models import Crud

admin.site.register(Crud)
class CrudAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'role']

# Register your models here.
