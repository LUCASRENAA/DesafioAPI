from rest_framework import serializers
from naner.models import   Author,Article




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializerCategory(serializers.ModelSerializer):
    author = AuthorSerializer

    class Meta:
        model = Article
        fields = ['id','author','category','title','summary']
        depth = 1


class ArticleSerializerAnonymousUser(serializers.ModelSerializer):
    author = AuthorSerializer

    class Meta:
        model = Article
        fields = ['id','author','category','title','summary','firstParagraph']
        depth = 1



class ArticleSerializerLoginUser(serializers.ModelSerializer):
    author = AuthorSerializer

    class Meta:
        model = Article
        fields = ['id','author','category','title','summary','firstParagraph','body']
        depth = 1



