from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    is_complete = models.BooleanField(default = False)
    created_by = models.CharField(max_length = 50)
    
