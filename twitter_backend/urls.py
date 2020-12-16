from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('profile/', include('user_profile.urls')),
    path('post/', include('post.urls')),
    path('notification/', include('notification.urls')),
    path('', include('home.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
