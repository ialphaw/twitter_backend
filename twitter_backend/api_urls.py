from rest_framework import routers

from search.views import ElasticSearch


router = routers.SimpleRouter()
router.register('', ElasticSearch, basename='search')
