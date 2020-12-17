from django.db import models

# Create your models here.
class Cart(models.Model):
    user = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    timestamp = models.DateTimeField()
    image = models.CharField(max_length=50)
    def __getitem__(self):
        return self.user

class shop(models.Model):
    brand = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    def __getitem__(self):
        return self.brand,self.price,self.img
