from django.contrib import admin
from .models import PizzaShop, Pizza, Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pizza', 'name', 'phone', 'date']

admin.site.register(PizzaShop)
admin.site.register(Pizza)
