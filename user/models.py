from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # one-one relation with existing user, CASCADE: if user is deleted remove profile not viceversa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add image in profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

