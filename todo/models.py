from django.db import models

# Create your models here.
class Item(models.Model): # Class item extends from the Model class
    name = models.CharField(max_length=30, blank=False) # We can have strings stored in here
    done = models.BooleanField(blank=False, default=False)
    
    def __str__(self):
        return self.name