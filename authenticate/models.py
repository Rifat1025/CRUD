from django.db import models

class SignUp(models.Model):
    u_name=models.CharField(max_length=20)
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    sex=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)

class LogIn(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


# Create your models here.
