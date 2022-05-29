from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from . import models

from rest_framework import viewsets, status
from . import serializers

def index(request):
    return HttpResponse("Done")

class TeamMemberNameView(viewsets.ModelViewSet):
    serializer_class = serializers.TeamMemberNameSerializer
    queryset = models.TeamMemberName.objects.all()

# Market Analyzer
from analysis.marketAnalyzer import marketAnalyzer

class marketView(viewsets.ModelViewSet):
    serializer_class = serializers.marketSerializer
    queryset = models.market.objects.all().order_by('-id')

    domain_keyword = str(queryset[0]).split(' ')[0]
    print("Domain Keyword : -->", domain_keyword)
    ma = marketAnalyzer()
    ma.getSentiments(domain_keyword)

    # serializer = serializers.marketAnalyzerSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()


# class marketAnalyzerView(viewsets.ModelViewSet):
#
#     def get_queryset(self):
#         serializer = serializers.marketAnalyzerSerializer()
#         company_name = serializer.data
#         return models.marketAnalyzer.objects.all()
#
#     def post(self, request, format=None):
#         serializer = serializers.marketAnalyzerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
