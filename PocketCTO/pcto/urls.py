from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'team_member_name', views.TeamMemberNameView, basename='team_name')
# router.register(r'market_analysis', views.marketView, basename='market_analysis')

urlpatterns = [
    path('index/', views.index, name="index"),
    path('', include(router.urls)),
    path('analyze/', views.analyzedata.as_view()),
]
