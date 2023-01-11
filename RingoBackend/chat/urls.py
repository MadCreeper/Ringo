from django.urls import path
from . import views
 
urlpatterns = [
     path('', views.index, name='index'),
     path('<str:room_name>/', views.room, name='room'),
     path('reset_msg', views.resetMsgView.as_view()),
     path('add_msg', views.addUnreadMsgView.as_view()),
]
 
