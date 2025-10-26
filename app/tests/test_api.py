import json
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from app.models import Dish, Menu
from app.serializers import DishSerializer


class DishAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='ali', password='123456')

        self.token_url = reverse('login')
        response = self.client.post(self.token_url, data={'username': 'ali', 'password': '123456'})
        token = response.data['token'] if 'token' in response.data else response.data.get('auth_token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        self.menu = Menu.objects.create(title='Main', description='Basic menu')
        self.dish1 = Dish.objects.create(name='Osh', menu=self.menu)
        self.dish2 = Dish.objects.create(name='Lagman', menu=self.menu)
        self.dish3 = Dish.objects.create(name='Manti', menu=self.menu)

    def test_get(self):
        url = reverse('dish-list')
        serializer = DishSerializer([self.dish1, self.dish2, self.dish3], many=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_filter(self):
        url = reverse('dish-list')
        serializer = DishSerializer([self.dish1], many=True)
        response = self.client.get(url, data={'name': 'Osh'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_search(self):
        url = reverse('dish-list')
        serializer = DishSerializer([self.dish1, self.dish3], many=True)
        response = self.client.get(url, data={'search': 'sh'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create(self):
        url = reverse('dish-list')
        data = {'name': 'Somsa', 'menu': self.menu.id}
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dish.objects.count(), 4)
        self.assertEqual(response.data.get('name'), 'Somsa')

    def test_update(self):
        url = reverse('dish-detail', args=(self.dish2.id,))
        data = {'name': 'Lagman Maxsusss', 'menu': self.menu.id}
        json_data = json.dumps(data)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.dish2.refresh_from_db()
        self.assertEqual(self.dish2.name, 'Lagman Maxsusss')

    def test_update_partial(self):
        url = reverse('dish-detail', args=(self.dish1.id,))
        data = {'name': 'Palov'}
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.dish1.refresh_from_db()
        self.assertEqual(response.data['name'], self.dish1.name)

    def test_delete(self):
        url = reverse('dish-detail', args=(self.dish3.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dish.objects.count(), 2)
