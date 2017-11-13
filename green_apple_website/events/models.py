from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=70)
    image = models.FileField()
    description = models.TextField()

    def __str__(self):
        return self.title
