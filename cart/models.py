from django.db import models
from .cart import Cart
from apps.user.models import User
from apps.orders.models import Order

class Customer(models.Model):
    user = models.ForeignKey(User, related_name = "user", on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, related_name='related_order')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)
