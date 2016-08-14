from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(
        max_length=100
    )
    code = models.CharField(
        max_length=100,
        unique=True
    )
    instructor = models.ForeignKey(
        User,
        null=True
    )

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.code)


class Question(models.Model):
    subject = models.ForeignKey(Subject)
    text = models.TextField()
    description = models.TextField(max_length=4000)

    def __unicode__(self):
        return "%s (%s)" % (self.text, self.subject)


class Option(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s (%s)" % (self.text, self.question)
