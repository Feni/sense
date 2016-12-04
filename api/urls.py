from django.conf.urls import url
from rest_framework import routers
from .views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'collections', CollectionsViewSet)
# router.register(r'dataset', DatasetViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^collections/(?P<collection_id>[-\w]+)/dataset$', CollectionDatasetViewSet.as_view(actions={'get': 'list'})),
    url(r'^collections/(?P<collection_id>[-\w]+)/dataset/(?P<row_id>[-\w]+)$', DatasetRowViewSet.as_view(actions={'get': 'list'})),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

