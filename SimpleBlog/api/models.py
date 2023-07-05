from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Post(models.Model):

    title= models.CharField(max_length=100)
    description=models.TextField()
    content= models.CharField(max_length=200)
    date_posted=models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title