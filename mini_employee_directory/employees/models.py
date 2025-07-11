from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
