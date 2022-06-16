from django.contrib import admin

from . models import *

class FamiliaresAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "edad", "fecha_nacimiento")

admin.site.register(Familiares, FamiliaresAdmin)
