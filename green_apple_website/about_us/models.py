from django.db import models


class MemberDetail(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
