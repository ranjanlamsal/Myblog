from django.db import models
from datetime import datetime
from django.db.models import Model

# Create your models here.
class Post(Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank= True)