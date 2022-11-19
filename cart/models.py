from django.db import models
from django.contrib.auth.models import User
from productapp.models import product


# Create your models here.
class CartItem(models.Model):
    cid = models.IntegerField(primary_key=True, auto_created=True)
    uid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pid = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    deliveryCharge = models.IntegerField(default=70)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.cid)
