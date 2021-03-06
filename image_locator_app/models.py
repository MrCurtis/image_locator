from django.db import models


class DroneImage(models.Model):
    image = models.FileField(upload_to='drone_images', blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    heading = models.FloatField()
    tilt = models.FloatField()
    roll = models.FloatField()
    water = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    shelter = models.BooleanField(default=False)
    medicine = models.BooleanField(default=False)
    protection = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
