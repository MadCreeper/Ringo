from tyadmin_api import auto_views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
    
router = DefaultRouter(trailing_slash=False)
    
router.register('permission', auto_views.PermissionViewSet)
    
router.register('group', auto_views.GroupViewSet)
    
router.register('content_type', auto_views.ContentTypeViewSet)
    
router.register('user_profile', auto_views.UserProfileViewSet)
    
router.register('verify_code', auto_views.VerifyCodeViewSet)
    
router.register('goods_category', auto_views.GoodsCategoryViewSet)
    
router.register('goods', auto_views.GoodsViewSet)
    
router.register('user_fav', auto_views.UserFavViewSet)
    
router.register('user_address', auto_views.UserAddressViewSet)
    
router.register('user_leaving_message', auto_views.UserLeavingMessageViewSet)
    
urlpatterns = [
        re_path('^', include(router.urls)),
    ]
    