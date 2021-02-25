from django.urls import path
from .views import HomeView, PostDetailView, PostCreateView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/create', PostCreateView.as_view(), name='post-create' ),
]
