from django.db import models

# Create your models here.
class newuser(models.Model):
	fname=models.CharField(max_length=100, blank=True)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=20)
	dob=models.CharField(max_length=20,blank=True)
	phone=models.IntegerField(blank=True)
	address=models.CharField(max_length=200,blank=True)


# class admin_new(models.Model):
# 	email=models.CharField(max_length=100)
# 	name=models.CharField(max_length=100, blank=True)
# 	subject=models.CharField(max_length=100, blank=True)
