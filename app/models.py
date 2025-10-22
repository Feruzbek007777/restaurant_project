from django.db import models


class Driver(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Dish(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    method = models.CharField(max_length=50)
    amount = models.BigIntegerField()

    def __str__(self):
        return f"{self.method} - {self.amount}"


class Delivery(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='deliveries')

    def __str__(self):
        return f"Delivery #{self.id}"


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='orders')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='orders')
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order #{self.id}"


class Like(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='likes')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=True)

    class Meta:
        unique_together = ('customer', 'dish')

    def __str__(self):
        return f"{self.customer} - {self.dish}"


class Comment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='comments')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return f"{self.customer} - {self.dish}"
