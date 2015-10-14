from django.db import models

class Company(models.Model):
    display_name = models.CharField(max_length=100, unique=True)

class Llc(models.Model):
    created_at = models.DateTimeField()
    dissolved = models.BooleanField()
    legal_name = models.CharField(max_length=100, unique=True)

class Fund(models.Model):
    bank_account_number = models.IntegerField()
    companies = models.ManyToManyField(Company, related_name="funds")
    is_single_asset = models.BooleanField()
    legal_name = models.CharField(max_length=100, unique=True)
    llc = models.ForeignKey(Llc, related_name="funds")
