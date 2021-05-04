from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)
    caption = models.TextField(max_length=280, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} ({self.user.username})'

    @property
    def imageUrl(self):
        return self.image.url

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})