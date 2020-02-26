from django.views import View
from django.shortcuts import render
from .serializer import UserLoginSerializer,UserRegistrationSerializer

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import UserLogin,Registration
from django.urls import reverse_lazy
from django.urls import reverse
from .models import Registration



class UserLoginViewset(viewsets.ModelViewSet):
      queryset = UserLogin.objects.all()
      serializer_class = UserLoginSerializer


class UserRegistrationViewset(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = UserRegistrationSerializer


class help(View):
     def get(self,request):
        return render(request,'index.html')



class redirect(View):
     def post(self,request):
         data1=request.POST.get('fname')
         User = {'data': data1}
         return render(request, 'sucess_logins.html', User)

class regpost(View):
       def post(self,request):
        u = request.POST['Username']
        p = request.POST['Password']
        e = request.POST['Email']
        User=Registration(Username=u,Password=p,Email=e)
        User.save()
       # context = { 'Username': u,'Password':p,'Email':e}
       # serializer = UserRegistrationSerializer(data=context)
       # if serializer.is_valid():
        #    serializer.save()
       # return JsonResponse(serializer.data, status=201)
        return render(request, 'regsuccess.html')





class your(View):
    def get(self,request):
        return render(request,'reg.html')
