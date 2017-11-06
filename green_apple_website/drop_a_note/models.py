from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    note = models.CharField(max_length=250)