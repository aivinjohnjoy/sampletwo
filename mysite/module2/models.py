from django.db import models

# Create your models here.

# Model to create a table moovie_tablepy in the DB
class moovie_tablepy(models.Model):
    Title=models.CharField(max_length=100)
    Year=models.IntegerField()
    Summary=models.TextField(max_length=1000)
    Success=models.BooleanField()
    Img=models.ImageField(upload_to='', null=True)
    def __str__(self):
        return self.Title        



