from django.db import models


# Create your models here.


class Contactus(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    phone = models.CharField(max_length=15, blank=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
