from django.contrib import admin

from .models import Customer, Dish, Order, Delivery, Driver, Payment, Menu

admin.site.register(Customer)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Driver)
admin.site.register(Payment)
admin.site.register(Menu)
