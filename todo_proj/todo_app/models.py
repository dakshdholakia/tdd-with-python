import django.utils as du
import datetime
from django.db import models
# Create your models here.

class Todo(models.Model):
    Title = models.CharField(max_length=100, blank=False, default="John Doe")
    Description = models.TextField(blank=True, default="Lorem Ipsum")
    Date = models.DateField(blank=False, default=du.timezone.now())
    Completed = models.BooleanField(default=False)

def __str__(self):
        return self.Title