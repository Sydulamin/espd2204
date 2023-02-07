from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    P_price = models.FloatField()
    description = models.TextField(max_length=500)
    quantity = models.PositiveIntegerField(default=1)
    pic = models.ImageField(upload_to='productPIC', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)
