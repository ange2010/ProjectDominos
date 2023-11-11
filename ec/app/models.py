from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATE_CHOICES = (
    ('Минская', 'Минская'),
    ('Могилевская', 'Могилевская'),
    ('Брестская', 'Брестская'),
    ('Гомельская', 'Гомельская'),
    ('Витебская', 'Витебская'),
    ('Гродненская', 'Гродненская'),
)
CATEGORY_CHOICES =(
    ('PZ', 'Пицца'),
    ('SA', 'Салаты'),
    ('DE', 'Десерты'),
    ('DR', 'Напитки'),
    ('SO', 'Соусы'),
    ('CH', 'Курица'),
    ('PA', 'Картофель'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    weight = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price


STATUS_CHOICES = (
    ('Принят', 'Принят'),
    ('Готов', 'Готов'),
    ('В пути', 'В пути'),
    ('Доставлен', 'Доставлен'),
    ('Отменен', 'Отменен'),
    ('Не подтвержден', 'Не подтвержден'),
)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Принят')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
