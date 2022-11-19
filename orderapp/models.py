from django.db import models
from cart.models import CartItem

# Create your models here.

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled'),
    ('In Stock', 'In Stack'),
    ('Out of Stock', 'Out of Stock')

)


class order(models.Model):
    oid = models.IntegerField(primary_key=True, auto_created=True)
    cartitem = models.ForeignKey(CartItem, on_delete=models.SET_NULL, null=True)
    uid = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    addr = models.TextField(max_length=100)
    town = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=6)
    phone = models.CharField(max_length=14)
    comment = models.TextField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return str(self.oid)
