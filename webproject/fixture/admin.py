from django.contrib import admin
from .models import Escuadra
# Register your models here.

class EscuadraAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Escuadra , EscuadraAdmin)
