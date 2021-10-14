from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.fields import CurrentUserDefault

from rest_framework import viewsets, generics
from rest_framework import status
from rest_framework.decorators import action, permission_classes, api_view, authentication_classes
from rest_framework.views import APIView

from naner.models import Author,Article
from naner.serializer import AuthorSerializer, ArticleSerializer, ArticleSerializer2, ArticleSerializer3
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, \
    BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView




from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        return request.user


class AuthorViewSet(viewsets.ModelViewSet):
    #requet.user
    """Listando todas as matrículas"""


    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ['get', 'post', 'put', 'path']

class ArticleViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly,UserPermission]
    queryset = Article.objects.all()



    serializer_class = ArticleSerializer
    def get_serializer_class(self):
        user = self.request.user
        print(user)
        try:
            if str(self.request.query_params['category']) != "":
                return ArticleSerializer
        except:
            if str(user) == "AnonymousUser":
                return ArticleSerializer2
            else:
                return ArticleSerializer3
    filter_backends = [DjangoFilterBackend]
    print("aqui")
    #print(UserPermission.has_permission())
    print(permission_classes)
    print(authentication_classes)
    filterset_fields = ['category']
    http_method_names = ['get', 'post', 'put', 'path']




@csrf_exempt
def login2(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return HttpResponse("sucess")
        else:
            return HttpResponse("failed")
    return HttpResponse("alo")

@csrf_exempt
def submit_registro(request):
    print(request.POST)
    if request.method == 'POST':
        senha = request.POST.get('password')
        usuario = request.POST.get ( 'username' )
        email =   request.POST.get ( 'email' )
        print(usuario)
        print(senha)
        try:
            user = User.objects.create_user ( str(usuario), str(email) ,  str(senha) )
            return HttpResponse('Sucess')

        except:
            #User.objects.get(usuario = usuario)
            #User.objects.get(email = email)
            return HttpResponse('Failed')


    return HttpResponse('<h1> faça um post </h1>')

