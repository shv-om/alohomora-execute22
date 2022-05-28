from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register()

urlpatterns = [
    path('', views.index, name="index"),
    path('name/', include(router.urls))
]
