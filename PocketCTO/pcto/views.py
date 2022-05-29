from django.shortcuts import render
from django.http import HttpResponse

from . import models

from rest_framework import viewsets
from . import serializers

def index(request):
    return HttpResponse("Done")

class TeamMemberNameView(viewsets.ModelViewSet):
    serializer_class = serializers.TeamMemberNameSerializer
    queryset = models.TeamMemberName.objects.all()

def Analyze():
    from ..analysis import marketAnalyzer
