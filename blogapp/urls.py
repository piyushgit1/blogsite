from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from blogapp.views import UserLoginView, UserRegisterView, ArticleGPDView, ArticlePublished, ArticleDraft, \
    ArticleRegisterdOneUser, ArticlePost, CommentPost, CommentFilterPublish, CommentFilterSpam, CommentUD, \
    LabelReturnAll, LableReturnViewByName

schema_view = get_schema_view(
    openapi.Info(
        title="Login views",
        default_version='v1',
    ),
    public=True,

)

app_name = "blogapp"
urlpatterns = [

    # TODO: https://pypi.org/project/django-environ/

    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('UserLoginView/<int:pk>/', UserLoginView.as_view()),
    path('UserLoginView/', UserLoginView.as_view()),
    path('UserRegisterView/', UserRegisterView.as_view()),
    path('ArticleGPDView/<int:pk>/', ArticleGPDView.as_view()),
    path('ArticlePublished/<int:pk>/', ArticlePublished.as_view()),
    path('ArticleDraft/<int:pk>/', ArticleDraft.as_view()),
    path('ArticleRegisterdOneUser/<int:pk>/', ArticleRegisterdOneUser.as_view()),
    path('ArticlePost/<int:pk>/', ArticlePost.as_view()),
    path('CommentPost/<int:pk>/', CommentPost.as_view()),
    path('CommentFilterPublish/<int:pk>/', CommentFilterPublish.as_view()),
    path('CommentFilterSpam/<int:pk>/', CommentFilterSpam.as_view()),
    path('CommentUD/<int:pk>/', CommentUD.as_view()),
    path('LabelReturnAll/<int:pk>/', LabelReturnAll.as_view()),
    path('LableReturnViewByName/<int:pk>/<Label>/', LableReturnViewByName.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
