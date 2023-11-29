from django.db import models

# Create your models here.
class Place(models.Model):



    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class Team1(models.Model):
    image=models.ImageField(upload_to='pics')
    name1 = models.CharField(max_length=250)
    descr1 = models.TextField()

    def __str__(self):
        return self.name1

