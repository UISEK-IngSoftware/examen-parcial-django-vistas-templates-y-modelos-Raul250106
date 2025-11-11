from django.db import models

# Create your models here.
class Movie (models.Model):
    name = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=30, null=False)
    director = models.CharField(max_length=30, null=False)
    year = models.DateField()
    sinopsis = models.TextField()
    def __str__(self):
        return self.name