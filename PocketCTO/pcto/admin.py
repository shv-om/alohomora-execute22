from django.contrib import admin
from . import models

class TeamMemberNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
admin.site.register(models.TeamMemberName, TeamMemberNameAdmin)
