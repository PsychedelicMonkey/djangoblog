from django.db import models
from django.contrib.auth.models import User
from hashlib import md5

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    background = models.ImageField(null=True, blank=True)
    about_me = models.TextField(max_length=500, null=True, blank=True)
    following = models.ManyToManyField(User, related_name='followers')

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

    def follow(self, user):
        if not self.is_following(user):
            self.following.add(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(id=user.id).count() > 0