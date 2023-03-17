from django.db import models

class employees(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=True, null=False)
    age = models.IntegerField(blank=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=False)
    number = models.IntegerField(blank=True, null=False)
    ethnicity = models.CharField(max_length=50, blank=True, null=False)
    phone = models.IntegerField(default=254773570102, blank=True, null=False)
    Amount = models.IntegerField(default= 0, blank=True, null=False)


def __str__(self):
    return self.name