from django.urls import path, include
from rest_framework import routers
from . import views

from rest_framework import routers

from .views import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')

urlpatterns = router.urls
