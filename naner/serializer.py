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
        #fields = '__all__'

        depth = 1


class ArticleSerializerAnonymousUser(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = ['id','author','category','title','summary','firstParagraph']
        depth = 1



'''
class ArticleSerializerLoginUser(serializers.HyperlinkedModelSerializer):
    #author = serializers.StringRelatedField()

    author = AuthorSerializer

    class Meta:
        model = Article
        fields = ['id','author','category','title','summary','firstParagraph','body']
        depth = 1
'''
class ArticleSerializerLoginUser(serializers.ModelSerializer):
    author = AuthorSerializer()


    class Meta:
        model = Article
        fields = ['id','author','category','title','summary','firstParagraph','body']


    def create(self, validated_data):

        category = str(validated_data['category'])
        title = str(validated_data['title'])
        summary = str(validated_data['summary'])
        firstParagraph = str(validated_data['firstParagraph'])
        body = str(validated_data['body'])


        try:
            user = Author.objects.get(name=str(validated_data['author']['name']))


        except:

            user = Author.objects.create( name=str(validated_data['author']['name']),
                picture=validated_data['author']['picture'])


        user = Article.objects.create(author=user,
                                      category=category,
                                      title=title,
                                      summary=summary,
                                      firstParagraph=firstParagraph,
                                      body=body)
        return user

    def update(self, instance,validated_data):
        #id = str(validated_data['id'])
        print(instance)
        print(validated_data)
        category = str(validated_data['category'])
        title = str(validated_data['title'])
        summary = str(validated_data['summary'])
        firstParagraph = str(validated_data['firstParagraph'])
        body = str(validated_data['body'])

        if str(instance.category) != str(category):
            instance.category = category
        if str(instance.title) != str(title):
            instance.title = title
        if str(instance.summary) != str(summary):
            instance.summary = summary
        if str(instance.firstParagraph) != str(firstParagraph):
            instance.firstParagraph = firstParagraph
        if str(instance.body) != str(body):
            instance.body = body

        try:
            user = Author.objects.get(name=str(validated_data['author']['name']))


        except:

            user = Author.objects.create(name=str(validated_data['author']['name']),
                                         picture=validated_data['author']['picture'])
        print(instance.author)
        print(user)
        instance.author = user
        #instance = instance.save()

        #article = Article.objects.get(id=id)
        #print(article)
        #return article

        return instance
