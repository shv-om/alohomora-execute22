from django.db import models
from django.contrib.auth.models import User

class Authenticate_info(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    dob = models.DateField()
    image = models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.user
