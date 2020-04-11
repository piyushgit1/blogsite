from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token

from blogapp.views import Blog_get_post, User_get_post, Blog_update_delete,User_update_delete,string,CommentView

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
    path('User_get_post/', User_get_post.as_view()),
    path('User_update_delete/<email_address>', User_update_delete.as_view()),
    path('Blog_get_post/<email_address>/', Blog_get_post.as_view()),
    path('Blog_upd_del/<email_address>/<post_title>/', Blog_update_delete.as_view()),
    path('Comments/<email_address>/<title_name>/', CommentView.as_view()),
    path('stirng',string.as_view())
]
