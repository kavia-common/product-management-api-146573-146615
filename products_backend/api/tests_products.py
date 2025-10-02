from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ProductCRUDTests(APITestCase):
    def setUp(self):
        self.list_url = "/api/products/"

    def test_health(self):
        url = reverse('Health')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, {"message": "Server is up!"})

    def test_create_list_retrieve_update_delete_product(self):
        # Create
        payload = {"name": "Laptop", "price": "999.99", "quantity": 5}
        resp = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        pid = resp.data["id"]

        # List
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(resp.data["count"], 1)

        # Retrieve
        detail_url = f"{self.list_url}{pid}/"
        resp = self.client.get(detail_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["name"], "Laptop")

        # Update (partial)
        resp = self.client.patch(detail_url, {"quantity": 7}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["quantity"], 7)

        # Delete
        resp = self.client.delete(detail_url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
