from django.db import models
from django.core.validators import MaxValueValidator


class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey('Tax', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def total_price(self):
        discount = (1 - self.discount.percent / 100) if self.discount else 1
        tax = (1 + self.tax.percent / 100) if self.tax else 1
        return float(self.price) * discount * tax

    @property
    def price(self):
        return sum([i.price for i in self.items.all()])
    
    def __str__(self) -> str:
        return f'{self.total_price} y.e.'


class Discount(models.Model):
    percent = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    
    def __str__(self) -> str:
        return str(self.percent)


class Tax(models.Model):
    percent = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def __str__(self) -> str:
        return str(self.percent)