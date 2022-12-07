from django.urls import path, include
from login.views import UserRegisterView, UserPasswordFoggotenView
urlpatterns=[
    path('register', UserRegisterView.as_view()),
    path('forget_password', UserPasswordFoggotenView.as_view()),
]