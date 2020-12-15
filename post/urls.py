from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('create-post', views.CreatePost.as_view()),
    path('show-hashtag-posts/<str:hashtag>', views.ViewHashtagPost.as_view()),
]
