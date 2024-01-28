from datetime import datetime
from django.db import models
from authentication import models as authent_model

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=60)
    quantity = models.IntegerField()
    product_id = models.CharField(max_length=5, blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default="", blank=True, null=True)
    image = models.ForeignKey("ProductImages", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(authent_model.User, on_delete=models.CASCADE)
    total_quantity = models.PositiveIntegerField()
    total_price = models.PositiveBigIntegerField()
    address = models.CharField(max_length=50, blank=True)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.user.email

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)


class PlaceOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    number_of_order = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to="place/order")

    def __str__(self):
        return f"{self.user.first_name} ordered {self.name}"


class ProductImages(models.Model):
    name = models.ImageField(_("Image for a product"), upload_to="product/images")
