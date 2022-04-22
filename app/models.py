from datetime import date
from re import T
from django.db import models

from app.views import topics

# Create your models here.
class post(models.Model):
    post_id=models.AutoField(primary_key=True)
    user_id =models.CharField(max_length=20)
    title=models.CharField(max_length=15)
    topic=models.CharField(max_length=30)
    post_date=models.DateField(auto_now_add=True)
    description=models.TextField()


