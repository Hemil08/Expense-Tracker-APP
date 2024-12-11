from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_expense = models.DateField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title
