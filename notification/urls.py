from django.urls import path

from . import views

app_name = 'notification'
urlpatterns = [
    path('notifs', views.Notification.as_view()),
]