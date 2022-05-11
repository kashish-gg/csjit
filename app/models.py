from django.db import models


# Create your models here.``
class post(models.Model):
    def __str__(self) -> str:
        return self.title
    post_id=models.AutoField(primary_key=True)
    user_id =models.CharField(max_length=20,default="---")
    title=models.CharField(max_length=15,default="---")
    emailid=models.CharField(max_length=35,default="---")
    gender=models.CharField(max_length=15,default="---")
    accountno=models.CharField(max_length=35,default="---")
    amount_paid=models.CharField(max_length=35,default="---")
    phone=models.CharField(max_length=10,default="---")
    topic=models.CharField(max_length=30,default="---")
    category=models.CharField(max_length=30,default="---")
    post_date=models.DateField(auto_now_add=True)
    description=models.TextField()


class topic(models.Model):
    def __str__(self) -> str:
        return self.title
    topic_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)

class date(models.Model):
    def __str__(self) -> str:
        return self.title
    date_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=40)
    date=models.CharField(max_length=20)