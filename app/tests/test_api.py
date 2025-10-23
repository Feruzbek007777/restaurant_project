from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from app.models import Driver, Delivery, Menu
from app.serializers import DeliverySerializer, MenuSerializer


class DeliveryApiTestCase(APITestCase):
    def test_get_all(self):
        driver = Driver.objects.create(name='Ali', phone='12345')
        d1 = Delivery.objects.create(driver=driver)
        d2 = Delivery.objects.create(driver=driver)
        url = reverse('delivery-list')
        response = self.client.get(url)
        serializer = DeliverySerializer([d1, d2], many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter(self):
        driver = Driver.objects.create(name='Ali', phone='12345')
        d1 = Delivery.objects.create(driver=driver)
        Delivery.objects.create(driver=driver)
        url = reverse('delivery-list') + f'?id={d1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(str(d1.id) in str(response.data)))


class MenuApiTestCase(APITestCase):
    def test_get_all(self):
        m1 = Menu.objects.create(title='Breakfast', description='Morning')
        m2 = Menu.objects.create(title='Dinner', description='Evening')
        url = reverse('menu-list')
        response = self.client.get(url)
        serializer = MenuSerializer([m1, m2], many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter(self):
        m1 = Menu.objects.create(title='Breakfast', description='Morning')
        Menu.objects.create(title='Dinner', description='Evening')
        url = reverse('menu-list') + '?title=Breakfast'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Breakfast' in str(response.data)))
