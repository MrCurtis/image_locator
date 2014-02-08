from django.db import models


class DroneImage(models.Model):

    image = models.FileField(upload_to='drone_images', blank=True)
    lattitude = models.FloatField()
    longtitude = models.FloatField()
    altitude = models.FloatField()
    heading = models.FloatField()
    tilt = models.FloatField()
    roll = models.FloatField()
    STATUS_TYPES = ( ('I', 'Important'), ('N', 'Nothing'), )
    status = models.CharField(max_length=1, choices=STATUS_TYPES, blank=True)
    interest_type = models.TextField(blank=True) 
    comment = models.TextField(blank=True)
    
  

    
    
