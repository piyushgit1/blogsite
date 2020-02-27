from django.shortcuts import render
from django.views import View
from rest_framework import viewsets

# TODO: bad practise to import using . (dot)
from .models import Registration
from .models import UserLogin
from .serializer import UserLoginSerializer, UserRegistrationSerializer


class UserLoginViewset(viewsets.ModelViewSet):
    # TODO: learn what is docstring and implement in all api as well as urls, implement swagger
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer


class UserRegistrationViewset(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = UserRegistrationSerializer


class help(View):
    def get(self, request):
        return render(request, 'index.html')


# TODO: class name must start with Capital letter
class redirect(View):
    def post(self, request):
        data1 = request.POST.get('fname')
        User = {'data': data1}
        return render(request, 'sucess_logins.html', User)


class regpost(View):
    def post(self, request):
        # TODO: User seriaiizer and check validity before accessing data
        # TODO: Very bad variable naming convention like u p e
        u = request.POST['Username']
        p = request.POST['Password']
        e = request.POST['Email']
        User = Registration(Username=u, Password=p, Email=e)
        User.save()
        # context = { 'Username': u,'Password':p,'Email':e}
        # serializer = UserRegistrationSerializer(data=context)
        # if serializer.is_valid():
        #    serializer.save()
        # return JsonResponse(serializer.data, status=201)
        return render(request, 'regsuccess.html')


class your(View):
    def get(self, request):
        return render(request, 'reg.html')
