from .models import Essay, Album, Files
from rest_framework import serializers


class EssaySerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    # 글만 작성하면 자동적으로 글쓴이(author_name)이 저장되게 하겠다.

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'content', 'author')


class AlbumSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    # 글만 작성하면 자동적으로 글쓴이(author_name)이 저장되게 하겠다.

    class Meta:
        model = Album
        fields = ('pk', 'image', 'desc', 'author')


class FileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    file = serializers.FileField(use_url=True)
    # 글만 작성하면 자동적으로 글쓴이(author_name)이 저장되게 하겠다.
    # FileField에 업로드한 것은 urls로 받겠다.

    class Meta:
        model = Files
        fields = ('pk', 'file', 'desc', 'author')