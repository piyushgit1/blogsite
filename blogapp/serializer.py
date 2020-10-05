from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from blogapp.models import User, Article, Comment


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Use to perform the serialize of json format data to queryset and save to database
    """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email']

    def validate_password(self, password):
        validate_password(password=password)
        return make_password(password)


class UserLoginSerializer(serializers.ModelSerializer):
    """
    Use to perform the serialize of json format data to queryset and save to database
    """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email']

    def validate_password(self, password):
        validate_password(password=password)
        return make_password(password)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'Label', 'body', 'updated_on', 'created_on', 'status', 'users']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'commenter_name', 'comment_body', 'comment_time', 'comment_choice', 'articles']
