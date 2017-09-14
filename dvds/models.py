from django.db import models

# Create your models here.
class Type_of(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Box(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Dvd(models.Model):
    name = models.CharField(max_length=255)
    type_of = models.ForeignKey(Type_of)
    location = models.ForeignKey(Box)

    def __str__(self):
        return self.name
