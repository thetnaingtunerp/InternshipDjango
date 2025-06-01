from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class IncomeExpense(models.Model):
    task_name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    task_detail = models.CharField(max_length=100, blank=True, null=True)
    date_upt = models.DateField(auto_now_add=True)
    amount1 = models.IntegerField()
    
    def __str__(self):
        return self.task_name




class MedicinesGroup(models.Model):
    name = models.CharField(max_length=100)
    

class Vaccie(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(MedicinesGroup, on_delete=models.CASCADE)
    



