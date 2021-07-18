from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=50)
    subject_id = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Names(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True

class Address(Names):
    address = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name


class Contact_Info(Names):
    contact = models.IntegerField()
    def __str__(self):
            return self.name
# Create your models here.
