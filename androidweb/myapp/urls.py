from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
]
