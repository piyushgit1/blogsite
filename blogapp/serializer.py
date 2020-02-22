from rest_framework  import  serializers
from .models import UserLogin

class UserLoginSerializer(serializers.ModelSerializer):
      class Meta:
          model=UserLogin
          fields= ['id','Username','Password']








