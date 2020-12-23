from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:primary_key>/', views.post_details, name='post_details'),
    path('post/new', views.post_new, name='post_new'),
    path('post/edit/<int:primary_key>', views.post_edit, name='post_edit'),
    path('post/delete/<int:primary_key>', views.post_delete, name='post_delete')
]