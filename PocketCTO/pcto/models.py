from django.db import models

class TeamMemberName(models.Model):
    name = models.CharField(max_length=25)
    department = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class market(models.Model):
    domain_keyword = models.CharField(max_length=25)

    def __str__(self):
        return self.domain_keyword
