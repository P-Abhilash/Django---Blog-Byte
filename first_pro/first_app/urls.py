from django.urls import path
from . import views

urlpatterns = [
    path('blog/',views.blog_post_list_view, name='blog_post_list_view'),
    path('blog/<str:slug>/',views.blog_post_detail_view, name='blog_post_detail_view'),
    path('blog/<str:slug>/edit/',views.blog_post_update_view, name='blog_post_update_view'),
    path('blog/<str:slug>/delete/',views.blog_post_delete_view, name='blog_post_delete_view'),
    path('blog-new/',views.blog_post_create_view, name='blog_post_create_view'),


    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]