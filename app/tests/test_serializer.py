from rest_framework.test import APITestCase
from app.models import Driver, Delivery, Menu
from app.serializers import DeliverySerializer, MenuSerializer


class DeliverySerializerTestCase(APITestCase):
    def test_get(self):
        driver = Driver.objects.create(name='Ali', phone='12345')
        d1 = Delivery.objects.create(driver=driver)
        d2 = Delivery.objects.create(driver=driver)

        data = [
            {'id': d1.id, 'driver': {'id': driver.id, 'name': 'Ali', 'phone': '12345'}},
            {'id': d2.id, 'driver': {'id': driver.id, 'name': 'Ali', 'phone': '12345'}}
        ]
        serializer = DeliverySerializer([d1, d2], many=True)
        self.assertEqual(serializer.data, data)


class MenuSerializerTestCase(APITestCase):
    def test_get(self):
        m1 = Menu.objects.create(title='Breakfast', description='Morning menu')
        m2 = Menu.objects.create(title='Dinner', description='Evening menu')

        data = [
            {'id': m1.id, 'title': 'Breakfast', 'description': 'Morning menu'},
            {'id': m2.id, 'title': 'Dinner', 'description': 'Evening menu'}
        ]
        serializer = MenuSerializer([m1, m2], many=True)
        self.assertEqual(serializer.data, data)
