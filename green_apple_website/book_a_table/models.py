from django.db import models


# from phonenumber_field.modelfields import PhoneNumberField


class BookDetail(models.Model):
    # number_of_persons = (('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5))

    customer = models.CharField(max_length=50, default="name")
    contact = models.IntegerField()
    email = models.EmailField(max_length=50, null=True)
    total_persons = models.CharField(max_length=4)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.customer + " -> " + str(self.id)
