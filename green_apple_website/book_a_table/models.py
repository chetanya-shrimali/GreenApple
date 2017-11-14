from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# from phonenumber_field.modelfields import PhoneNumberField


class BookDetail(models.Model):
    customer = models.CharField(max_length=50, default="name")
    contact = models.IntegerField(validators=[MinValueValidator(6000000000), MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=50, null=True)
    total_persons = models.CharField(max_length=4)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.customer + " -> " + str(self.id)
