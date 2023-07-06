from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from Account.models import Customer, Manager
from rest_framework import status
from django.contrib.auth import get_user_model
import json
import io
import random

from PIL import Image
from django.core.files.base import ContentFile
from django.test import TestCase


class UnauthorizedTest(APITestCase):

    def setUp(self) -> None:
        new_user1 = {
            "email": "amin@gmail.com",
            "phone_number": "09133630096",
            "role": "C",
            "password": "ILOVEDJANGO"
        }
        new_user2 = {
            "email": "ali@gmail.com",
            "phone_number": "09133630095",
            "role": "M",
            "password": "ILOVEDJANGO"
        }

        new_user3 = {
            "email": "reza@gmail.com",
            "phone_number": "09133630092",
            "role": "A",
            "password": "ILOVEDJANGO"
        }
        self.user1 = get_user_model().objects.create_user(**new_user1)
        self.user1.is_active = True
        self.user1.save()
        self.token1 = Token.objects.create(user=self.user1)

        self.user2 = get_user_model().objects.create_user(**new_user2)
        self.user2.is_active = True
        self.user2.save()
        self.token2 = Token.objects.create(user=self.user2)

        self.user3 = get_user_model().objects.create_user(**new_user3)
        self.user3.is_active = True
        self.user3.save()
        self.token3 = Token.objects.create(user=self.user3)

    def set_credential(self, token):
        """
            set token for authorization
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    # /ticket/myticket/
    # def test_user_can_get_myticket(self):
    #     """
    #         test user can get myticket
    #     """
    #     self.set_credential(token=self.token1)
    #     response = self.client.get("/ticket/myticket/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_manager_cannot_get_myticket(self):
    #     """
    #         test manager cannot get myticket
    #     """
    #     self.set_credential(token=self.token2)
    #     response = self.client.get("/ticket/myticket/")
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cannot_cancelreserve(self):
        """
            test user cannot cancel reserve
        """
        # self.set_credential(self.token1)
        response = self.client.post("/api/hotel/cancelreserve/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_cannot_createhotel(self):
        """
            test user cannot create hotel
        """
        self.set_credential(token=self.token1)
        data = {
            "name": "Parsian",
            "phone_number": "0912345678",
            "description": "Nice Hotel",
            "country": "Iran",
            "city": "Esfahan",
            "longitude": 0,
            "latitude": 0,
            "address": "Esfahan, Iran"
        }
        response = self.client.post("/api/hotel/hotel/", data)
        # self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_get_hotels(self):
        self.set_credential(token=self.token1)
        response = self.client.get("/api/hotel/myhotels/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_manager_can_get_hotels(self):
        self.set_credential(token=self.token2)
        response = self.client.get("/api/hotel/myhotels/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_manager_cannot_addcomment(self):
        self.set_credential(token=self.token2)
        response = self.client.post("/comment/addcomment/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_addcomment(self):
        self.set_credential(token=self.token1)
        response = self.client.post("/comment/addcomment/")
        # just check authorization
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_replycomment(self):
        self.set_credential(token=self.token1)
        response = self.client.post("/comment/reply/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_manager_can_replycomment(self):
        self.set_credential(token=self.token2)
        response = self.client.put("/comment/reply/1")
        # just check authorization
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    # def test_user_cannot_getcommentstag(self):
    #     self.set_credential(token=self.token1)
    #     response = self.client.get("/comment/tag/")
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_manager_can_getcommentstag(self):
    #     self.set_credential(token=self.token2)
    #     response = self.client.get("/comment/tag/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_user_cannot_getadmintickets(self):
    #     self.set_credential(token=self.token1)
    #     response = self.client.get("/ticket/admin_ticket_list/")
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_manager_can_getadmintickets(self):
    #     self.set_credential(token=self.token2)
    #     response = self.client.get("/ticket/admin_ticket_list/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def generate_photo_file(self):
        file = io.BytesIO()
        r = random.Random().random()
        image = Image.new('RGB', size=(100, 100), color=(
            130, int(r * 120), int(10 + 5 * r)))
        file.name = './test.png'
        image.save("test.png", 'PNG')

        file.seek(0)
        return file

    def test_hotel_creation_with_image(self):
        self.set_credential(token=self.token2)
        data = {'manager': '1',
                'name': '"mamad"',
                'country': '"iran"',
                'city': '"jjjjjjjj"',
                'address': '"dddd"'}
        hotel_image = self.generate_photo_file()
        data['files'] = [
            ('files', (hotel_image.name, hotel_image, 'image/png'))]

        # # add hotel_image to request as multipart/form-data

        self.set_credential(self.token1)
        response = self.client.post(
            "/api/hotel/hotel/", data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hotel_creation_without_image(self):
        self.set_credential(token=self.token2)
        data = {'manager': '1',
                'name': '"mamad"',
                'country': '"iran"',
                'city': '"jjjjjjjj"',
                'address': '"dddd"'}
        self.set_credential(self.token1)
        response = self.client.post("/api/hotel/hotel/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hotel_creation_without_required_fields(self):
        self.set_credential(token=self.token2)
        data = {'country': '"iran"',
                'city': '"jjjjjjjj"',
                'address': '"dddd"'}
        self.set_credential(self.token1)
        response = self.client.post("/api/hotel/hotel/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_hotel_creation_with_invalid_manager(self):
        self.set_credential(token=self.token2)
        data = {'manager': '9999',
                'name': '"mamad"',
                'country': '"iran"',
                'city': '"jjjjjjjj"',
                'address': '"dddd"'}
        self.set_credential(self.token1)
        response = self.client.post("/api/hotel/hotel/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
