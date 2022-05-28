from rest_framework import serializers
from . import models

class TeamMemberNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMemberName
        fields = ('id', 'name', 'department')
