from django.db import models


class UserLogin(models.Model):
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)