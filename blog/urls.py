from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:primary_key>/', views.post_details, name='post_details'),
    path('post/new', views.post_new, name='post_new')
]