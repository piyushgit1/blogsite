"""Creating of Views for the Rest api call

First viewset created userloginviewset which perform the crud

"""

from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from blogapp.permissions import IsPostOrIsAuthenticated
from blogapp.models import User, Post, Comment
from blogapp.serializer import UserLoginSerializer, UserRegisterSerializer, BlogSerializer, CommentSerializer


################################################################################################################

class User_get_post(APIView):
    permission_classes = [IsPostOrIsAuthenticated, ]

    def get(self, request):
        """ Used to get the username registered
        """
        usernames = User.objects.all()
        serializers = UserLoginSerializer(usernames, many=True)
        return Response(request, serializers.data, status=203)

    def post(self, request):
        """takes the data and provide the input"""
        data = JSONParser().parse(request)
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)


class User_update_delete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    """ used to update and delete any user """

    def put(self, request, email_address):
        """
        updates the profile of the user
        """

        data = JSONParser().parse(request)
        user_obj = User.objects.get(email=email_address)
        serializer = UserRegisterSerializer(user_obj, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request, email_address):
        user_obj = User.objects.get(email=email_address)
        user_name = user_obj.username
        user_obj.delete()
        return Response({user_name}, "deleted successfully")


#####################################################################################################################

class Blog_get_post(APIView):
    """
    Use to Provide the Create, retreive , update and delete
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        blogcontent = Post.objects.all()
        serializers = BlogSerializer(blogcontent, many=True)
        return Response(serializers.data, status=203)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)


class Blog_update_delete(APIView):
    permission_classes = [permissions.IsAuthenticated, ]


""" Email address is used to filter particular post made by user as many user can have same username
    Post_title will filter that post with the given title"""


def put(self, request, email_address, post_title):
    data = JSONParser().parse(request)
    obj = Post.objects.filter(blogging__email=email_address, title=post_title)
    serializer = BlogSerializer(obj, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=201)


def delete(self, request, email_address, post_title):
    obj = Post.objects.filter(blogging__email=email_address, title=post_title)
    obj.delete()
    return Response("Object Deleted")


######################################################################################################################

class CommentView(APIView):
    """
      Comment viewset for crud
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        data = Post.objects.filter(Commas__comment_key_id=1)
        serializer = BlogSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, title_name):
        data = JSONParser().parse(request)
        obj = Post.objects.get(title=title_name)
        Comment_object_creator = Comment.objects.create(comment_key=obj)
        serializer = CommentSerializer(Comment_object_creator, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# class Comment_update_delete(APIView):

#  def put(self,request,post_title):


class string(APIView):

    def get(self, request):
        username = "hi"
        return Response(username)
