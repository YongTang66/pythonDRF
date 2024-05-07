from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, PhoneViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'phones', PhoneViewSet, basename='phone')

urlpatterns = [
    path('', include(router.urls)),
]