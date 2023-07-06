from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from .models import TicketForm, RequestForm
from Hotel.models import Hotel
from rest_framework import status
from django.contrib.auth import get_user_model
import json


class Ticket(APITestCase):
    def setUp(self) -> None:
        
                    new_user1 ={
                        "email": "amin@gmail.com",
                        "phone_number": "09133630096",
                        "role": "C",
                        "password": "ILOVEDJANGO"
    }
                    new_user2 ={
                        "email": "ali@gmail.com",
                        "phone_number": "09133630095",
                        "role": "M",
                        "password": "ILOVEDJANGO"
    }
                    
                    new_user3 ={
                        "email": "reza@gmail.com",
                        "phone_number": "09133630092",
                        "role": "A",
                        "password": "ILOVEDJANGO"
    }
                
                        
                    self.user1 =get_user_model().objects.create_user(**new_user1)
                    self.user1.is_active=True
                    self.user1.save()
                    self.token1 = Token.objects.create(user=self.user1)
                    
                    
                    
                    self.user2 =get_user_model().objects.create_user(**new_user2)
                    self.user2.is_active=True
                    self.user2.save()
                    self.token2 = Token.objects.create(user=self.user2)
                    
                    
                    self.user3 =get_user_model().objects.create_user(**new_user3)
                    self.user3.is_active=True
                    self.user3.save()
                    self.token3 = Token.objects.create(user=self.user3)
                    
                    
                    
    def set_credential(self, token):
            """
                set token for authorization
            """
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_is_not_None(self):
        request1=self.client.get(reverse("nearhotel"),self.myloc1).json()
        request2=self.client.get(reverse("nearhotel"),self.myloc2).json()
        request3=self.client.get(reverse("nearhotel"),self.myloc3).json()
        
        self.assertNotEqual(request1,None)
        self.assertNotEqual(request2,None)
        self.assertNotEqual(request3,None)
        pass 
    def test_result(self):
        
        request1=self.client.get(reverse("nearhotel"),self.myloc1).json()
        request2=self.client.get(reverse("nearhotel"),self.myloc2).json()
        request3=self.client.get(reverse("nearhotel"),self.myloc3).json()
        
        self.assertEqual([2,3],[i["id"] for i in request1])
        self.assertEqual([2,3],[i["id"] for i in request2])
        self.assertEqual([1],[i["id"] for i in request3])
    
    def test_length_is_ok_but_result_not_ok(self):
        request1=self.client.get(reverse("nearhotel"),self.myloc1).json()
        request2=self.client.get(reverse("nearhotel"),self.myloc2).json()
        request3=self.client.get(reverse("nearhotel"),self.myloc3).json()
        r1=[i["id"] for i in request1]
        r2=[i["id"] for i in request2]
        r3=[i["id"] for i in request3]
        self.assertEqual(len(r1),2)
        self.assertTrue(1 not in r1)
        self.assertEqual(len(r2),2)
        self.assertTrue(1 not in r2)
        self.assertEqual(len(r3),1)
        self.assertTrue(2 not in r3)
    
    def test_withot_parametr(self):
        request1=self.client.get(reverse("nearhotel")).json()
        r1=[i["id"] for i in request1]
        self.assertEqual([2,3],r1)
        self.assertNotEqual(r1,None)
        self.assertNotEqual(r1,[])

    def test_status_code(self):
        request1=self.client.get(reverse("nearhotel"),self.myloc1)
        request2=self.client.get(reverse("nearhotel"),self.myloc2)
        request3=self.client.get(reverse("nearhotel"),self.myloc3)
        
        self.assertEqual(request1.status_code,200)
        self.assertEqual(request2.status_code,200)
        self.assertEqual(request3.status_code,200)