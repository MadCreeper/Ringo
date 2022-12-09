from django.urls import path, include
from login.views import UserRegisterView, UserPasswordFoggotenView,UserPasswordChangeView
urlpatterns=[
    path('register', UserRegisterView.as_view()),
    path('forget_password', UserPasswordFoggotenView.as_view()),
    path('reset_password', UserPasswordChangeView.as_view()),
]