from django.db import models

# Create your models here.

class Level(models.Model):
    title= models.CharField(max_length=20)

    def __str__(self):
        return self.title



class Student(models.Model):
    name = models.CharField(max_length=30)
    usn = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=30)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)

    def __str__(self):
        return self.name