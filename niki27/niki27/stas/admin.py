from django.contrib import admin
from .models import *


class ValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'jsonb')
    ist_display_links = ('id', 'name')
    search_fields = ('id', 'name',)


admin.site.register(Value, ValueAdmin)
