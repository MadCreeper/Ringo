from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('needs', views.NeedsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', views.hello, name='hello'),
]