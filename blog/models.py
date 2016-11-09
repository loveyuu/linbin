from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampedModel):
    tag_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tag_name


class Post(TimeStampedModel):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

