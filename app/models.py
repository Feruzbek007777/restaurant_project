from django.db import models


class Driver(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    def __str__(self):
        return f"Delivery #{self.id}"


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id}"
