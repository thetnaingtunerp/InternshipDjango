from django.contrib import admin
from .models import *
# Register your models here.

class IncomeExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_name', 'amount', 'category', 'date']
    list_filter = ['category', 'date']
    search_fields = ['task_name', 'amount']

admin.site.register(Category)
admin.site.register(IncomeExpense, IncomeExpenseAdmin)