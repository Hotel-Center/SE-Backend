from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model
import json
import decimal

class BalanceSer(APITestCase):
        def setUp(self) -> None:
                        new_user1 ={
                            "email": "amin@gmail.com",
                            "phone_number": "09133630096",
                            "role": "C",
                            "password": "ILOVEDJANGO",
                          
        }
                        new_user2 ={
                            "email": "ali@gmail.com",
                            "phone_number": "09133630095",
                            "role": "M",
                            "password": "ILOVEDJANGO",
                            
        }                 
                        
                        new_user3 ={
                            "email": "reza@gmail.com",
                            "phone_number": "09133630092",
                            "role": "A",
                            "password": "ILOVEDJANGO",
                        
        }
                    
                            
                        self.user1 =get_user_model().objects.create_user(**new_user1)
                        self.user1.is_active=True
                        self.user1.balance=decimal.Decimal(1.5)
                        self.user1.save()
                        self.token1 = Token.objects.create(user=self.user1)
                        
                        
                        
                        self.user2 =get_user_model().objects.create_user(**new_user2)
                        self.user2.is_active=True
                        self.user2.balance=decimal.Decimal(2.5)
                        self.user2.save()
                        self.token2 = Token.objects.create(user=self.user2)
                        
                        
                        self.user3 =get_user_model().objects.create_user(**new_user3)
                        self.user3.is_active=True
                        self.user3.balance=decimal.Decimal(3.5)
                        self.user3.save()
                        self.token3 = Token.objects.create(user=self.user3)
                        
                        
                        
                        
        def set_credential(self, token):
                """
                    set token for authorization
                """
                self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

            
        def test_get_balance_notpermission_auth(self):
            request1=self.client.get("/api/accounts/balance/")
            self.assertEqual(request1.status_code
                             ,401)
            
        def test_get_balance(self):
            self.set_credential(token=self.token2)
            request1=self.client.get("/api/accounts/balance/")
            self.assertEqual(request1.status_code,200)
            self.assertEqual(decimal.Decimal(request1.json()['balance']),2.50)
        
        def test_increase_balance_notpermission(self):
            request1=self.client.get("/api/accounts/balance/")
            self.assertEqual(request1.status_code
                             ,401)
        
        def test_increase_balance(self):
            self.set_credential(token=self.token1)
            before_increase=self.user1.balance
            request1=self.client.patch("/api/accounts/balance/",{"amount":decimal.Decimal(2)})
            self.assertEqual(request1.status_code,200)
            self.assertEqual(decimal.Decimal(request1.json()['balance']),before_increase+2)
            
     
        
            
        
         
          
            
        
            
            
            
          
       