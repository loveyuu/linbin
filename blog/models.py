from __future__ import unicode_literals

from django.db import models


class TimeStampedModel(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
