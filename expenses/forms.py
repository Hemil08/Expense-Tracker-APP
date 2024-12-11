from django import forms
from .models import Expense,Category

class ExpenseForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget= forms.RadioSelect,
        required=False,
    )

    class Meta:
        model = Expense
        fields = [
            "title",
            "amount",
            "date_of_expense",
            "category",
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "description"
        ]