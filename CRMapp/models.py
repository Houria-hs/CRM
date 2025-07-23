from django.db import models

# Create your models here.

# the customer model
class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length= 15)
    adresse = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    

# leads model
class leads(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    Last_Contacted_Date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.customer
