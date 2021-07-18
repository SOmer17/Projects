from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    rollnumber = models.IntegerField()
    graduated = models.BooleanField()

    def __str__(self):
        return self.name
