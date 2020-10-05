from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def get_short_name(self):
        return self.username


class Article(models.Model):
    STATUS = (("Draft", "Default"), ("Publish", "Publish"))

    users = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="Article",
                              related_query_name="Art")
    title = models.CharField(max_length=250)
    Label = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    COMMENT_CHOICES = (("Publish", "Publish"), ("Spam", "Spam"))

    articles = models.ForeignKey(Article, null=True, on_delete=models.CASCADE, related_name='Comment',
                                 related_query_name='Commas')
    commenter_name = models.CharField(max_length=20)
    comment_body = models.CharField(max_length=1000)
    comment_time = models.DateTimeField(auto_now=True)
    comment_choice = models.CharField(max_length=200, choices=COMMENT_CHOICES)
