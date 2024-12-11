from rest_framework import serializers
from expenses.models import Category,Expense

# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description']

# Serializer for the Expense model
class ExpenseSerializer(serializers.ModelSerializer):
    category  = CategorySerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ['id','title','amount','date_of_expense','category']



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
