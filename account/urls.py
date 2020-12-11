from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('create-account', views.CreateAccount.as_view()),
]
