from django.urls import path, include
from login.views import UserRegisterView
urlpatterns=[
    path('register', UserRegisterView.as_view())
]