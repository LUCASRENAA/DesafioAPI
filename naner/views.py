from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


from naner.models import Author,Article
from naner.serializer import AuthorSerializer, \
    ArticleSerializerCategory, ArticleSerializerAnonymousUser, ArticleSerializerLoginUser

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import  DjangoModelPermissionsOrAnonReadOnly




from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        return request.user


class AuthorViewSet(viewsets.ModelViewSet):


    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ['get', 'post', 'put', 'path']

class ArticleViewSet(viewsets.ModelViewSet):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly,UserPermission]
    queryset = Article.objects.all()



    serializer_class = ArticleSerializerLoginUser
    def get_serializer_class(self):
        user = self.request.user
        print(user)
        try:
            if str(self.request.query_params['category']) != "":
                return ArticleSerializerCategory
        except:
            if str(user) == "AnonymousUser":
                return ArticleSerializerAnonymousUser
            else:
                return ArticleSerializerLoginUser
    filter_backends = [DjangoFilterBackend]
    print("aqui")
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
            return HttpResponse('401 Unauthorized', status=401)
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

            return HttpResponse('400 Bad Request', status=400)


    return HttpResponse('<h1> faça um post </h1>')

