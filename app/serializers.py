from rest_framework import serializers
from .models import Driver, Delivery, Customer, Order, Dish, Menu, Payment


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = Delivery
        fields = '__all__'
        depth = 1


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()

    class Meta:
        model = Dish
        fields = '__all__'
        depth = 1

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    dish = DishSerializer()
    payment = PaymentSerializer()
    delivery = DeliverySerializer()

    class Meta:
        model = Order
        fields = '__all__'

#nested serializerni qolladim xulas u depthga oxshab ketarkan yani u barcha malumotni bittada ob kelarkan 