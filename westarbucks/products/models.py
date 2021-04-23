from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = "products"
# Create your models here.
