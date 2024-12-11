from django.contrib import admin
from .models import Expense,Category

# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title","amount","date_of_expense")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","description")