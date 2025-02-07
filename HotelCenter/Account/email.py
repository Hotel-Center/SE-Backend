from djoser import email
from djoser import utils
from djoser.conf import settings
from django.contrib.auth.tokens import default_token_generator  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Account.models import User


class ActivationEmail(email.ActivationEmail):
    template_name = 'email/emailVerification.html'

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)
        return context
    