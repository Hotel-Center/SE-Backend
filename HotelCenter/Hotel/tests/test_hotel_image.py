import http
import os
import io
import random
from datetime import timedelta, date

from django.utils.datetime_safe import datetime
from rest_framework import status, reverse
from PIL import Image
from django.core.files import File
from django.http import HttpResponseBadRequest
from django.core.files.base import ContentFile
from django.test import TestCase
import json
from django.utils.http import urlencode

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from ..models import Hotel, HotelImage, Room, roomFacility, Reserve, FavoriteHotel


class HotelTestCase(APITestCase):

    def setUp(self) -> None:
        """
            RUNS BEFORE EACH TEST
        """

        self.test_root = os.path.abspath(os.path.dirname(__file__))
        self.facility1 = {"name": "free_wifi"}
        self.facility2 = {"name": "parking"}

        self.hotel_data1 = {
            "name": "Parsian",
            "phone_number": "0912345678",
            "description": "Nice Hotel",
            "country": "Iran",
            "city": "Esfahan",
            "longitude": 0,
            "latitude": 0,
            "address": "Esfahan, Iran"
        }

        self.hotel_data2 = {
            "name": "Ferdosi",
            "city": "Khorasan",
            "country": "Iran",
            "check_in": "15:00",
            "check_out": "12:00",
            "description": "with best view of the city and places",
            "phone_number": "09123456709",
            'rate': 4.4,
            "address": "Khorasan,Iran"
        }

        self.user1 = get_user_model().objects.create(
            is_active=True, email="user1@gmail.com")
        self.user1.set_password("some-strong1pass")
        self.user1.role = "M"
        self.user1.save()

        self.user2 = get_user_model().objects.create(
            is_active=True, email="user2@gmail.com")
        self.user2.set_password("some-strong2pass")
        self.user2.save()

        self.user3 = get_user_model().objects.create(
            is_active=True, email="user3@gmail.com")
        self.user3.set_password("some-strong3pass")
        self.user3.save()

        self.token1 = Token.objects.create(user=self.user1)
        self.token2 = Token.objects.create(user=self.user2)
        self.token3 = Token.objects.create(user=self.user3)

    def set_credential(self, token):
        """
            set token for authorization
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def unset_credential(self):
        """
            unset existing headers
        """
        self.client.credentials()


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
    hotel_image = self.generate_photo_file()

    # add image to data
    data['files'] = hotel_image

    self.set_credential(self.token1)
    response = self.client.post("/api/hotel/hotel/", data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
