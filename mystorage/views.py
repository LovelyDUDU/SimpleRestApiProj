from django.shortcuts import render
from rest_framework import viewsets
from mystorage.models import Essay, Album, Files
from mystorage.serializer import EssaySerializer, AlbumSerializer, FileSerializer
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

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

from rest_framework.response import Response
from rest_framework import status

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer

    parser_classes = (MultiPartParser, FormParser) # 다양한 media 타입으로 request를 수락.
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

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)