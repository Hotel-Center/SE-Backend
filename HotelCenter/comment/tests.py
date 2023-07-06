from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from Account.models import Customer,Manager
from Hotel.models import Hotel
from .models import Tag, Comment, Reply
from rest_framework import status
from django.contrib.auth import get_user_model
import json


class CommentTest(APITestCase):
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
                    
                    
    
                    hotel_data1 = {
                            "name": "Parsian",
                            "phone_number": "0912345678",
                            "description": "Nice Hotel",
                            "country": "Iran",
                            "city": "Esfahan",
                            "longitude": 2,
                            "latitude": 1,
                            "address": "Esfahan, Iran"
                            }
                        
                    hotel_data2 = {
                            "name": "Ferdosi",
                            "city": "Khorasan",
                            "country": "Iran",
                            "check_in": "15:00",
                            "check_out": "12:00",
                            "description": "with best view of the city and places",
                            "phone_number": "09123456709",
                            'rate': 4.4,
                            "address": "Khorasan,Iran",
                            "longitude": 0.25,
                            "latitude": 0.25,
                        }
                    hotel_data3 = {
                            "name": "amirkabir",
                            "city": "Kashan",
                            "country": "Iran",
                            "check_in": "15:00",
                            "check_out": "12:00",
                            "description": "with best view of the city and places",
                            "phone_number": "09132001683",
                            'rate': 4.4,
                            "address": "Khorasan,Iran",
                            "longitude": 0.1,
                            "latitude": 0.1,
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
                    
                    self.h1=Hotel.objects.create(manager=self.user2,**hotel_data1)
                    self.h2=Hotel.objects.create(manager=self.user2,**hotel_data2)
                    self.h3=Hotel.objects.create(manager=self.user2,**hotel_data3)
                    
                    self.tag1=Tag.objects.create(name="tag1")
                    self.tag2=Tag.objects.create(name="tag2")
                    self.tag3=Tag.objects.create(name="tag3")
                    
                    
                    self.comment1=Comment.objects.create(writer=self.user1,text="text1",hotel= self.h1)
                    self.comment2=Comment.objects.create(writer=self.user1,text="text2",hotel= self.h1)
                    self.comment3=Comment.objects.create(writer=self.user1,text="text3",hotel= self.h1)
                    
                    self.reply1=Reply.objects.create(text_reply="text_reply1")
                    self.reply2=Reply.objects.create(text_reply="text_reply2")
                    
                    self.comment1.reply=self.reply1
                    self.comment1.save()
                    self.comment2.reply=self.reply2
                    self.comment2.save()
                    
                    
                    
    def set_credential(self, token):
            """
                set token for authorization
            """
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_str_tag(self):
            self.assertEqual(self.tag1.name,"tag1")
            self.assertEqual(self.tag2.name,"tag2")
            self.assertEqual(self.tag3.name,"tag3")
        
    def test_str_comment(self):
            self.assertEqual(self.comment1.text,"text1")
            self.assertEqual(self.comment2.text,"text2")
            
    def test_tag_notpermission(self):
         request1=self.client.get("/comment/tag/")
         self.assertEqual(request1.status_code
                             ,401)
    
    def test_tag_haspermission(self):
        self.set_credential(token=self.token2)
        request1=self.client.get("/comment/tag/")
        self.assertEqual(request1.status_code
                             ,200)
    
    def test_new_comment_nopermission_Iscustomer(self):
        request1=self.client.post("/comment/addcomment/",{"writer":1,"hotel":1,"text":"hello"})
        self.assertEqual(request1.status_code
                             ,401)
    def test_new_comment2_nopermission(self):
        self.set_credential(token=self.token2)
        request1=self.client.post("/comment/addcomment/",{"writer":1,"hotel":1,"text":"hello"})
        self.assertEqual(request1.status_code
                             ,403)
                               
    def test_new_comment_ok(self):
        self.set_credential(token=self.token1)
        request1=self.client.post("/comment/addcomment/",{"writer":1,"hotel":1,"text":"hello"})
        self.assertEqual(request1.status_code
                             ,200)
        
         
         
        
        
        
           
            