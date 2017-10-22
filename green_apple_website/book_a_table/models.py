from django.db import models


class BookDetail(models.Model):
    number_of_persons = (('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5))

    total_persons = models.CharField(max_length=4, choices=number_of_persons, default='1')
    date = models.DateField(null=False)
    time = models.TimeField()
