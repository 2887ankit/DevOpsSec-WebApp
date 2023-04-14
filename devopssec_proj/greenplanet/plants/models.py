from django.db import models

# Create your models here.
class Plant(models.Model): # each class variable represents a database i.e. table field in the model 
    name = models.CharField(max_length=200) 
    country = models.CharField(max_length=50) 
    climate = models.CharField(max_length=200) 
    soil = models.CharField(max_length=200) 
    family = models.CharField(max_length=200)
    height = models.FloatField()
    user_id = models.CharField(max_length=100, null=True)
    
    def __str__(self): 
        return self.name + "- " + self.country