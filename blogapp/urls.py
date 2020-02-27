from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'UserRecord', views.UserLoginViewset)
router.register(r'Registration', views.UserRegistrationViewset)

app_name = "blogapp"
urlpatterns = [
    # TODO: naming convention is very bad, learn how to name url according to rest framework guideline
    # TODO: https://pypi.org/project/django-environ/

    path('api/', include(router.urls)),
    path('ind', views.help.as_view()),
    path('login', views.redirect.as_view(), name="login"),
    path('api/UserRecored/<int:pk>/', views.UserLoginViewset),
    path('regist', views.regpost.as_view(), name="regist"),
    path('reg', views.your.as_view())
    # path('get_post', views.View_Post_list.as_view()),
    # path('post', views.poster),

    #  path('put_delete/v1',views.update_delete_list.as_view()),

]
