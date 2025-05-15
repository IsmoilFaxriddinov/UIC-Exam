from rest_framework import generics
from django.views.generic import TemplateView

from users.models import RegisterModel
from users.serializer import RegisterSerializer


class UserView(TemplateView):
    template_name = 'main.html'
    context_object_name = 'users'

class RegisterView(generics.CreateAPIView):
    queryset = RegisterModel
    template_name = 'register.html'
    serializer_class = RegisterSerializer