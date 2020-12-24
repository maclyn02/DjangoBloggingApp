from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:primary_key>/', views.post_details, name='post_details'),
    path('post/new/', views.post_new, name='post_new'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/publish/<int:primary_key>/', views.post_publish, name='post_publish'),
    path('post/edit/<int:primary_key>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:primary_key>/', views.post_delete, name='post_delete'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.post_list, name='post_list'),

    path('post/<int:primary_key>/comment/', views.comment_create, name='comment_create'),
    path('post/<int:primary_key>/comment/<int:comment_key>/like', views.like_comment, name='like_comment'),
    path('post/<int:primary_key>/comment/<int:comment_key>/dislike', views.dislike_comment, name='dislike_comment'),
    path('post/<int:primary_key>/comment/<int:comment_key>/delete', views.delete_comment, name='delete_comment'),
    path('post/<int:primary_key>/comment/<int:comment_key>/approve', views.approve_comment, name='approve_comment'),
    path('signup/', views.signup, name='signup'),

]
