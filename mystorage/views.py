from django.shortcuts import render
from rest_framework import viewsets
from mystorage.models import Essay, Album, Files
from mystorage.serializer import EssaySerializer, AlbumSerializer, FileSerializer
from rest_framework.filters import SearchFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all().order_by('title')
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'content',)

    # 내가 직접 작성한 객체의 user를 자동으로 저장.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated and self.request.user.is_staff:
            qs = qs.all()
        elif self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    filter_backends = [SearchFilter]
    search_fields = ('desc', 'author',)

    # 내가 직접 작성한 객체의 user를 자동으로 저장.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated and self.request.user.is_staff:
            qs = qs.all()
        elif self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer

    filter_backends = [SearchFilter]
    search_fields = ('desc', 'author',)

    # 내가 직접 작성한 객체의 user를 자동으로 저장.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated and self.request.user.is_staff:
            qs = qs.all()
        elif self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs

    # parser_class 지정
    # create() 오버라이딩딩