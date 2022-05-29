from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from . import models

import os
import csv
import json

from rest_framework import viewsets, status
from . import serializers

def index(request):
    return HttpResponse("Done")

class TeamMemberNameView(viewsets.ModelViewSet):
    serializer_class = serializers.TeamMemberNameSerializer
    queryset = models.TeamMemberName.objects.all()

# Market Analyzer
# from analysis.marketAnalyzer import *

class marketView(viewsets.ModelViewSet):
    serializer_class = serializers.marketSerializer
    queryset = models.mAnalyzer.objects.all().order_by('-id')
    if queryset:
        domain_keyword = str(queryset[0]).split(' ')[0]
        print("Domain Keyword : -->", domain_keyword)
        # ma = marketAnalyzer()
        # ma.getSentiments(domain_keyword)


# Market Analysis Data
# defining the function to convert CSV file to JSON file
def convjson(csvFilename):
    mydata = {}

    # reading the data from CSV file
    with open(csvFilename, encoding = 'utf-8') as csvfile:
        csvRead = csv.DictReader(csvfile)
        # Converting rows into dictionary and adding it to data

        for rows in csvRead:
            key = rows.keys()
            val = rows.values()
            mydata['value'] = list(key)[0]
            mydata['count'] = list(val)[0]

            print(mydata)

    # dumping the data
    return json.dumps(mydata)


class analyzedata(APIView):

    def get(self, request):
        path = "D:/Shivam/alohomora-execute22/PocketCTO/pcto/sample1/"
        dir_list = os.listdir(path)
        context_processor = []

        for file in dir_list:
            csv_file = os.path.join(path, file)
            context_processor.append(convjson(csv_file))

        return Response({'context_processor' : context_processor})
