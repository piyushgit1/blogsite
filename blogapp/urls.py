from django.urls import include , path
from  .import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'UserRecord',views.UserLoginViewset)


urlpatterns=[

         path('api/',include(router.urls)),
        #path('get_post', views.View_Post_list.as_view()),
        #path('post', views.poster),

      #  path('put_delete/v1',views.update_delete_list.as_view()),

]