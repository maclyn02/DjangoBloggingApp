from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:primary_key>/', views.post_details, name='post_details'),
]