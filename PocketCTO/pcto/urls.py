from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'team_member_name', views.TeamMemberNameView)

urlpatterns = [
    path('', views.index, name="index"),
    path('name/', include(router.urls))
]
