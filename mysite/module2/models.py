from django.db import models

# Create your models here.

class moovie_tablepy(models.Model):
    Title=models.CharField(max_length=100)
    Year=models.IntegerField()
    Summary=models.TextField(max_length=1000)
    Success=models.BooleanField()
    def __str__(self):
        return self.Title        



