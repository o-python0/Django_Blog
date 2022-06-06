from django.db import models

from django.contrib.auth.models import User

class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to='', null=True, blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readText = models.TextField(null=True, blank=True, default=User.username)

    def __str__(self):
        return self.title


