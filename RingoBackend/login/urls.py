from django.urls import path, include
from login.views import UserRegisterView, UserPasswordForgottenView,UserPasswordChangeView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns=[
    path('register', UserRegisterView.as_view()),
    path('forget_password', UserPasswordForgottenView.as_view()),
    path('reset_password', UserPasswordChangeView.as_view()),
    path('login', obtain_jwt_token)
]