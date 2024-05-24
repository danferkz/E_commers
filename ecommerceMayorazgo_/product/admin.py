from django.contrib import admin
from . models import Products
from . models import Categories
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(Products, SimpleHistoryAdmin)
admin.site.register(Categories)
