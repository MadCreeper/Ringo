from django.db import models

class Needs(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30, blank=True, null=True)