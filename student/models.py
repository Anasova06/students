from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    AUID = models.CharField(unique=True)
    section = models.CharField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
