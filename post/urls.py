from django.urls import path
from . import views


urlpatterns = [
    path('user/post/', views.PostListCreateAPIView.as_view()),
    path('postd/', views.PostDetailAPIView.as_view()),
]