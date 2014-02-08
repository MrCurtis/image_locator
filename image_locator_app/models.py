from django.db import models

class SelectedImage(models.Model):

    image = models.FileField(upload_to = 'drone_images', blank = True)
    lattitude = models.FloatField()
    longtitude = models.FloatField()
    comment = models.TextField()
    
class RawImages(models.Model):

    filename = models.TextField()
    image = models.FileField(upload_to = 'drone_images', blank = True)
    lattitude = models.FloatField()
    longtitude = models.FloatField()

    
    
