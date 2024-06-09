from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns=[
    #path('', views.index, name='index'),
    path('', PostListView.as_view(), name='post-list'),
    path('<book_id>', views.detail, name='books_detail'),
    path('<int:post_id>', views.post_detail),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]
