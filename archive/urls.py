from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('', PostListView.as_view(), name="archive"),
]