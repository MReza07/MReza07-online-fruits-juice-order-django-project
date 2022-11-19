from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class product(models.Model):
    pid = models.BigIntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    price = models.FloatField()
    discounted_price = models.FloatField(default=10)
    deliveryCharge = models.IntegerField(default=70)
    weight = models.FloatField()
    category = models.CharField(max_length=25)
    delivery = models.SmallIntegerField(default=7)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='upload')

    def __str__(self):
        return str(self.pid)


class review_rating(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pid = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rate = models.FloatField()
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
