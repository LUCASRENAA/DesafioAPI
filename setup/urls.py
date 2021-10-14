from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path

from naner import views
from naner.views import ArticleViewSet, AuthorViewSet
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from setup import settings

router = routers.DefaultRouter()

router.register('api/article', views.ArticleViewSet, basename='article')
router.register('api/author', AuthorViewSet, basename='author')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('', include(router.urls) ),

    path('api/login/', views.login2),
        path('api/sign-up/', views.submit_registro),

    path('api-auth/', include('rest_framework.urls')),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
