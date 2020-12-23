from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:primary_key>/', views.post_details, name='post_details'),
    path('post/new', views.post_new, name='post_new'),
    path('drafts', views.post_draft_list, name='post_draft_list'),
    path('post/publish/<int:primary_key>', views.post_publish, name='post_publish'),
    path('post/edit/<int:primary_key>', views.post_edit, name='post_edit'),
    path('post/delete/<int:primary_key>', views.post_delete, name='post_delete')
]