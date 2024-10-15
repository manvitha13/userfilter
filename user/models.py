from django.db import models

# Create your models here.
class userdetailes(models.Model):
    userid=models.IntegerField()
    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Adharno=models.BigIntegerField()
    panno=models.CharField(max_length=100)
    Emailid=models.EmailField()
    place=models.CharField(max_length=100)
    contactno=models.BigIntegerField()
    photo=models.ImageField(upload_to="images/")
class Meta:
    db_table="userdetailes"