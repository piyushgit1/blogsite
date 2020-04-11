from django.contrib.auth.models import AbstractUser
from django.db import models

STATUS = (("Publish", "Publish"), ("Repost", "Repost"))



class Post(models.Model):
    title = models.CharField(max_length=250, default='titile')
    body = models.TextField(default="Write here")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_key = models.ForeignKey(Post, null=True, on_delete=models.DO_NOTHING, related_name='Comment',
                                 related_query_name='Commas')
    commenter_name = models.CharField(max_length=20)
    comment_body = models.CharField(max_length=1000)
    comment_time = models.DateTimeField(auto_now=True)


class Label(models.Model):
    post_label = models.ForeignKey(Post, null=True, on_delete=models.DO_NOTHING)
    label_name = models.CharField(max_length=200)


class User(AbstractUser):
    blog = models.ForeignKey(Post, null=True, on_delete=models.CASCADE,related_name="blog",related_query_name="blogging")

    def get_short_name(self):
        return self.username
