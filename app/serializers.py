from rest_framework import serializers
from .models import Driver, Delivery, Customer, Order, Dish, Menu, Payment, Like, Comment


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'
        depth = 1


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    dish = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'customer', 'dish', 'text']


class DishSerializer(serializers.ModelSerializer):
    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(), source='menu', write_only=True
    )

    menu = MenuSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = ['id', 'name', 'menu', 'menu_id', 'likes', 'dislikes', 'comments']

    def get_likes(self, instance):
        return instance.likes.filter(like=True).count()

    def get_dislikes(self, instance):
        return instance.likes.filter(like=False).count()


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


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'like', 'dish', 'customer']
        read_only_fields = ['customer']
