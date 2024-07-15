from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from sales_network.models import Link, Product
from users.models import User


class ProductAPITest(APITestCase):

    def setUp(self):
        # Создание пользователя
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.pro', is_active=True)
        self.user.set_password('qqqwww111222')

        self.client.force_authenticate(user=self.user)

        # Создание продукта
        self.product = Product.objects.create(
            title="test_product",
            model="test_model",
            release_date="2024-08-15"
        )

    def test_create_product(self):
        """Тест создания продукта."""
        data = {
            "title": "test_title",
            "model": "test_model",
            "release_date": "2024-08-15"
        }

        response = self.client.post(
            reverse('sales_network:products-list'),
            data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_product(self):
        """Тест вывода всех продуктов."""
        response = self.client.get(
            reverse('sales_network:products-list')
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_product(self):
        """Тест частичного редактирования продукта."""
        updated_data = {
            "model": "Updated model"
        }

        response = self.client.patch(
            reverse('sales_network:products-detail', args=[self.product.id]), updated_data
        )

        self.product.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        """Тест редактирования продукта."""
        updated_data = {
            "title": "Test_name",
            "model": "Test_model",
            "release_date": "2024-08-20"
        }

        response = self.client.put(
            reverse('sales_network:products-detail', args=[self.product.id]), updated_data
        )

        self.product.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        """Тест отображения одного продукта."""
        response = self.client.get(
            reverse('sales_network:products-detail', args=[self.product.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        """Тест удаления продукта."""
        response = self.client.delete(
            reverse('sales_network:products-detail', args=[self.product.id])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LinkAPITest(APITestCase):

    def setUp(self):
        # Создание пользователя
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.pro', is_active=True)
        self.user.set_password('qqqwww111222')

        self.client.force_authenticate(user=self.user)

        # Создание продукта
        self.product = Product.objects.create(
            title="test_product",
            model="test_model",
            release_date="2024-08-15"
        )

        self.all_prod = Product.objects.all()

        # Создание звена
        self.link = Link.objects.create(
            title="test_link",
            email="test@test.ru",
            country="test_country",
            city="test_city",
            provider=None,
            debt="500.5",
            create_time="2024-08-15"
        )

        self.link.save()
        self.link.product.add(*self.all_prod.values_list("id", flat=True))

    def test_create_link(self):
        """Тест создания звена сети."""
        data = {
            "title": "test_link",
            "email": "test1@test.ru",
            "country": "test_country",
            "city": "test_city",
            "product": [self.product.id, ],
            "provider": self.link.id,
            "debt": "7000"
        }

        response = self.client.post(
            reverse('network:link-create'),
            data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_link(self):
        """Тест вывода списка звеньев сети."""
        response = self.client.get(
            reverse('network:link-list')
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_link(self):
        """Тест редактирования звена сети."""
        updated_data = {
            "country": "Updated country"
        }

        response = self.client.patch(
            reverse('network:link-update', args=[self.link.id]), updated_data
        )

        self.link.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_link(self):
        """Тест вывода одного звена сети."""
        response = self.client.get(
            reverse('network:link-get', args=[self.link.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_link(self):
        """Тест удаления цепочки сети."""
        response = self.client.delete(
            reverse('network:link-delete', args=[self.link.id])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
