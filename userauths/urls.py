from django.urls import path
from .views import *

urlpatterns =[
    path('sign-up/', RegisterView, name="sign_up"),
]