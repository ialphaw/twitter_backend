from django.urls import path

from . import views

app_name = 'user_profile'
urlpatterns = [
    path('show-my-profile', views.ShowProfile.as_view()),
    path('show-user-profile/<str:username>', views.ShowUserProfile.as_view()),
    path('follow-user', views.FollowUser.as_view()),
]