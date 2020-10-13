from django.core.mail import send_mail
from django.db.models import Count
from django.http import Http404
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from blogapp.models import User, Article, Comment
from blogapp.serializer import UserLoginSerializer, UserRegisterSerializer, ArticleSerializer, CommentSerializer
from blogsite.settings import EMAIL_HOST_USER

"""####### 
 LOGIN VIEW ##################   """


class UserLoginView(APIView):
    """ Can view the registered account and update also delete"""

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        """ Used to get the username registered
        """

        user_object = self.get_object(pk)
        serializer = UserLoginSerializer(user_object)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        """takes the data and provide the input"""

        data = JSONParser().parse(request)
        user_obj = self.get_object(pk)
        serializer = UserLoginSerializer(user_obj, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):

        """ Delete the requested Userobject present in the database """
        user_obj = self.get_object(pk)
        username = user_obj.username
        user_obj.delete()
        return Response("Successfully Deleted {},Redirect to Login Page".format(username))


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    """ For registration purpose only """

    def post(self, request, format=None):
        """
        Register the user
        """

        data = JSONParser().parse(request)
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        send_mail("{} Registerd ".format(data['username']),
                  "Visit to website", EMAIL_HOST_USER, [data['email']], fail_silently=False)
        return Response(serializer.data, status=201)


""" #################### ARTICLE VIEWSET ############################## """


class ArticlePost(APIView):
    """
        Article Register is done
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        data = JSONParser().parse(request)
        data['users'] = pk
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)


class ArticleGPDView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    """ Get Put and Delete the Article by a user"""

    def get_object(self, pk, format=None):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article_obj = self.get_object(pk)
        serializers = ArticleSerializer(article_obj)
        return Response(serializers.data, status=203)

    def put(self, request, pk, format=None):
        data = JSONParser().parse(request)
        article_obj = self.get_object(pk)
        serializer = ArticleSerializer(article_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        article_obj = self.get_object(pk)
        article_username = article_obj.title
        article_obj.delete()
        return Response("{} successfully deleted".format(article_username))


class ArticleDraft(APIView):
    """ Provide the response bassed on status
        two status are present 1.draft 2.publish for article """

    def get(self, request, pk, format=None):
        article_obj_status = Article.objects.filter(users_id=pk, status='Draft')
        serializer = ArticleSerializer(article_obj_status, many=True)
        return Response(serializer.data, status=201)


class ArticlePublished(APIView):
    """ Provide the response bassed on status
        two status are present 1.draft 2.publish for article """

    def get(self, request, pk, format=None):
        article_obj_status = Article.objects.filter(users_id=pk, status='Publish')
        serializer = ArticleSerializer(article_obj_status, many=True)
        return Response(serializer.data, status=201)


class ArticleRegisterdOneUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    """ Total number of article return by one user"""

    def get_object(self, pk, format=None):
        try:
            User.objects.filter(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Article_obj_all = Article.objects.filter(users_id=pk)
        serializer = ArticleSerializer(Article_obj_all, many=True)
        return Response(serializer.data, status=201)


""" #################### COMMENT VIEWSETE ############################## """


class CommentPost(APIView):
    """
        Comment Post is done for any article
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, pk, format=None):
        data = JSONParser().parse(request)
        data['articles'] = pk
        serializer = CommentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CommentFilterPublish(APIView):
    """
        Comment are filterd by based on status and all Published comment by a user on all article returns

    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        b = Comment.objects.filter(articles__users__pk=pk, comment_choice='Publish')
        serializer = CommentSerializer(b, many=True)
        return Response(serializer.data)


class CommentFilterSpam(APIView):
    """ all spam comments on all artilce by a user"""
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        comment_obj = Comment.objects.filter(articles__users__pk=pk, comment_choice='Spam')
        serializer = CommentSerializer(comment_obj, many=True)
        return Response(serializer.data)


class CommentUD(APIView):
    """
     To delete and update the comment
    """

    def put(self, request, pk, format=None):
        data = JSONParser().parse(request)
        comment_obj = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment_obj, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        comment_obj = Comment.objects.filter(pk=pk)
        comment_obj.delete()
        return Response("Comment Deleted")


class LabelReturnAll(APIView):
    permission_classes = [permissions.IsAuthenticated]

    """ It returns the article grouped label with same value and have couted part assigned """

    def get(self, request, pk, format=None):
        response = Article.objects.filter(users__pk=pk)
        v = response.values('Label').order_by('Label').annotate(counts=Count('Label'))
        return Response(v, status=201)


class LableReturnViewByName(APIView):
    permission_classes = [permissions.IsAuthenticated]
    """ Gives the article object based on label"""


    def get(self, request, pk, Label, format=None):
        Label_obj = Article.objects.filter(users__pk=pk, Label=Label)
        serializer = ArticleSerializer(Label_obj, many=True)
        return Response(serializer.data)
