from django.urls import path

from . import views

app_name = 'recombee'
urlpatterns = [
    path('create', views.create_user_db),
]
