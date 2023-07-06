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
                        
                        
                        self.re1=RequestForm.objects.create(name="Re1")
                        self.re2=RequestForm.objects.create(name="Re2")
                        self.re3=RequestForm.objects.create(name="Re3")
                        
                        self.ti1=TicketForm.objects.create(sender=self.user1,text="text1",request=self.re1)
                        self.ti2=TicketForm.objects.create(sender=self.user2,text="text2",request=self.re2)
                        
                        
        def set_credential(self, token):
                """
                    set token for authorization
                """
                self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        def test_str_Request(self):
            self.assertEqual(self.re1.name,"Re1")
            self.assertEqual(self.re2.name,"Re2")
            self.assertEqual(self.re3.name,"Re3")
        
        def test_str_ticket(self):
            self.assertEqual(self.ti1.text,"text1")
            self.assertEqual(self.ti2.text,"text2")
            
        def test_request_list_notpermission_auth(self):
            request1=self.client.get("/ticket/new_type_request/")
            self.assertEqual(request1.status_code
                             ,401)
        
        def test_request_list_not_admin(self):
            self.set_credential(token=self.token2)
            request1=self.client.get('/ticket/new_type_request/')
            self.assertEqual(request1.status_code,403)
        
        def test_request_list_not_admin(self):
            self.set_credential(token=self.token3)
            request1=self.client.get('/ticket/new_type_request/')
            self.assertEqual(request1.status_code,200)
            self.assertEqual([i['id'] for i in request1.json()],[1,2,3])
            
        def test_request_list_not_admin(self):
            self.set_credential(token=self.token3)
            request1=self.client.get('/ticket/new_type_request/')
            self.assertEqual(request1.status_code,200)
            self.assertEqual([i['id'] for i in request1.json()],[1,2,3])
            
        def test_request_add_new_req(self):
            self.set_credential(token=self.token3)
            request1=self.client.post('/ticket/new_type_request/',{"name":"req5"})
            self.assertEqual(request1.status_code,201)
            self.assertEqual(request1.json()['id'],4)
            self.assertEqual(request1.json()['name'],"req5")
        
        def test_request_add_new_req(self):
            self.set_credential(token=self.token1)
            request1=self.client.post('/ticket/myticket/',{"sender":1,"text":"text__4","request":1})
            self.assertEqual(request1.status_code,201)
            self.assertEqual(request1.json()['id'],3)
            self.assertEqual(request1.json()['text'],"text__4")
            
        def test_request_add_new_req(self):
            self.set_credential(token=self.token3)
            request1=self.client.get('/ticket/admin_ticket_list/')
            self.assertEqual(request1.status_code,200)
            
        
            
        
         
          
            
        
            
            
            
          
       