from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    brand_store = models.TextField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=500)
    average_rating = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=50)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    total_value_of_the_order = models.FloatField()
    purchase_date = models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_details = models.ForeignKey(Order, on_delete=models.CASCADE)
    estimated_date_of_delivery_of_each_product = models.DateTimeField()
    quantity = models.IntegerField(default=1)


class CostomerPanDetail(models.Model):
    customer_name = models.OneToOneField(Customer, on_delete=models.CASCADE)
    pan_number = models.CharField(max_length=13)
    name_of_customer = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    pan_details_are_verified = models.BooleanField(default=False)
