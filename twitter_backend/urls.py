from django.contrib import admin
from django.urls import path, include

from search.views import ElasticSearch
from .api_urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('profile/', include('user_profile.urls')),
    path('post/', include('post.urls')),
    path('notification/', include('notification.urls')),
    path('search/', include(router.urls)),
    path('recombee/', include('recombee.urls')),
    path('', include('home.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
