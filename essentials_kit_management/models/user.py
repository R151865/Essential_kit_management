from django.db import models

from django.contrib.auth.models import AbstractUser

from essentials_kit_management.constants.enums import FormStatusEnum


class User(AbstractUser):
    name = models.CharField(max_length=300)
    is_admin = models.BooleanField(default=False)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    min_quantity = models.IntegerField(default=0)
    max_quantity = models.IntegerField()
    price_per_item = models.IntegerField()


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    items = models.ForeignKey(Item, on_delete=models.CASCADE)


class Form(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(
        choices=[(status.name, status.value) for status in FormStatusEnum],
        max_length=10
        )
    description = models.TextField()
    close_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField(null=True)
    sections = models.ForeignKey(Section, on_delete=models.CASCADE)


class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ForeignKey(Item, on_delete=models.CASCADE)
   brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
   form = models.ForeignKey(Form, on_delete=models.CASCADE)
   section = models.ForeignKey(Section, on_delete=models.CASCADE)
   count = models.IntegerField(default=0)
   pending_count = models.IntegerField()
   out_of_stock = models.IntegerField()