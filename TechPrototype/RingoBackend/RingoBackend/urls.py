"""RingoBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from goods.views import GoodsListViewSet, GoodsCategoryViewset
from user_operation.views import  UserOfferingViewset, UserNeedsViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
import RingoBackend.settings as settings
import user_operation.views as opView


router = DefaultRouter()

router.register(r'apis/goods', GoodsListViewSet, basename="goods")


# 配置Offerings的url
router.register(r'apis/offering', UserOfferingViewset, basename="offering")

router.register(r'apis/category', GoodsCategoryViewset, basename="category")

router.register(r'apis/need', UserNeedsViewset, basename="need")

urlpatterns = [
    re_path('^', include(router.urls)),
    path('docs/', include_docs_urls(title='RingoApis')),
    path('admin/', admin.site.urls),
    path('apis/login/', include('login.urls')),
    path('apis/user_profile', opView.PersonalProfileView.as_view())
    # path('apis/jwt-token-auth/', obtain_jwt_token),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
