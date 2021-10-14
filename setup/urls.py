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

    path('login/', views.login2),
    path('registro/', views.submit_registro),

    path('login2/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
    #path('rest_auth/registration/', include('rest_auth.registration.urls'))

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
