from rest_framework import serializers
from . import models

class TeamMemberNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMemberName
        fields = ('id', 'name', 'department')

class marketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.manalyzer
        fields = ('id', 'domain_keyword')
