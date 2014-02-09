from django.db import models


class DroneImage(models.Model):

    image = models.FileField(upload_to='drone_images', blank=True)
    lattitude = models.FloatField()
    longtitude = models.FloatField()
    altitude = models.FloatField()
    heading = models.FloatField()
    tilt = models.FloatField()
    roll = models.FloatField()
    
    water = models.BooleanField(initial=False)
    sanitation = models.BooleanField(initial=False)
    food = models.BooleanField(initial=False)
    shelter = models.BooleanField(initial=False)
    medicine = models.BooleanField(initial=False)
    protection = models.BooleanField(initial=False)
    obstruction = models.BooleanField(initial=False) 
    comment = models.TextField(blank=True)
    
  

    
    
