from django.db import models

# Create your models here.
class Hygiene_Complaint(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    cdh = models.CharField(max_length=50)
    complaint = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.cdh + '     ' +  self.name
    
class Finance_Complaint(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    complaint = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.name
    
class Menu_Complaint(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    cdh = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    complaint = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.cdh + '     ' +  self.item

class Staff_Complaint(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    cdh = models.CharField(max_length=50)
    complaint = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.cdh + '     ' +  self.name
    
class Icafe_Complaint(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    icafe = models.CharField(max_length=50)
    complaint = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.icafe + '     ' +  self.name
    
    
class Menu(models.Model):
    Menu_Item = models.CharField(max_length=100)
    def __str__(self):
        return self.Menu_Item
    
class CDH(models.Model):
    cdh = models.CharField(max_length=100)
    def __str__(self):
        return self.cdh
    
class Icafe(models.Model):
    icafe = models.CharField(max_length=100)
    def __str__(self):
        return self.icafe