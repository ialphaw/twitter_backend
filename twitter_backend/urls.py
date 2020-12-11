from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('profile/', include('user_profile.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
