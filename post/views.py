from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import UserFavouriteSerializer, UserCartSerializer ,Postserializer
from .models import UserCart, UserFavorite ,Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = Postserializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    permission_classes = [IsAuthenticated]