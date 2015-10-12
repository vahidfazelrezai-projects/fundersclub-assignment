from django.db import models

class Fund(models.Model):
    bank_account_number = models.IntegerField()
    companies = models.CharField(max_length=100)
    is_single_asset = models.BooleanField()
    legal_name = models.CharField(max_length=100)
    llc = models.CharField(max_length=100)

class Company(models.Model):
    display_name = models.CharField(max_length=100)
    created_at = models.DateField()

class Llc(models.Model):
    created_at = models.DateField()
    dissolved = models.BooleanField()
    legal_name = models.CharField(max_length=100)
