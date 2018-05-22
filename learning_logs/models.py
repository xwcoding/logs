from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """return a string representation of the model"""
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:     #extra information to manage a model
        verbose_name_plural = 'entries'     # use entries when it needs to refer to more than one entry

    def __str__(self):
        return self.text[:50] + "..."   #show first 50 chars