from django.db import models
from accounts.models import CustomUser as User
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart #{self.id} for {self.user.username}'

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity}x {self.product} in {self.cart}'
