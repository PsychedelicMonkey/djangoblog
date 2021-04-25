from django.db import models
from django.contrib.auth.models import User
from hashlib import md5

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    background = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def imageUrl(self):
        try:
            img = self.image.url
        except:
            digest = md5(self.user.email.lower().encode('utf-8')).hexdigest()
            img = f'https://www.gravatar.com/avatar/{digest}?d=identicon'
        return img

    @property
    def backgroundUrl(self):
        try:
            img = self.background.url
        except:
            img = ''
        return img