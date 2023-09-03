from django.urls import path
from .views import *

urlpatterns =[
    path('sign-up/', RegisterView, name="sign_up"),
    path('sign-out/', logoutView, name="sign_out"),
    path('sign-in/', loginView, name="sign_in"),
]