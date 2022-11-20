from django.contrib import admin

from app.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass