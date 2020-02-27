from django.db import models


class UserLogin(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)


class Registration(models.Model):
    Username1 = models.CharField(max_length=50)
    Password2 = models.CharField(max_length=50)
    # TODO: column name should not be in capital letter
    # TODO: lean different type of model fields, like here it should be models.UrlField
    Email = models.CharField(max_length=254)
