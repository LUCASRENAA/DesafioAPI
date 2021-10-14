from rest_framework import serializers
from naner.models import   Author,Article




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer

    class Meta:
        model = Article
        fields = ['id','author','category','title','summary']
        #,'firstParagraph','body'
        depth = 1


class ArticleSerializer2(serializers.ModelSerializer):
    author = AuthorSerializer

    class Meta:
        model = Article
        fields = ['id','author','category','title','summary','firstParagraph']
        #,'','body'
        depth = 1



class ArticleSerializer3(serializers.ModelSerializer):
    author = AuthorSerializer

    class Meta:
        model = Article
        fields = ['id','author','category','title','summary','firstParagraph','body']
        #,'firstParagraph','body'
        depth = 1



