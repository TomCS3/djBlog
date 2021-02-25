from django.urls import path
from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/create', PostCreateView.as_view(), name='post-create' ),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]
