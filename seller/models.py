from django.db import models

# Create your models here.
class Seller(models.Model):
    name=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    mob=models.PositiveIntegerField(null=True)
    password=models.TextField(max_length=100,null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table='seller'

class Category(models.Model):
    name=models.TextField(max_length=100,null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.TextField(max_length=50,null=True)
    price=models.FloatField(null=True)
    image=models.ImageField(upload_to='products',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        self.name
    
    class Meta:
        db_table='product'
