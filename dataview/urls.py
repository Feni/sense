from django.conf.urls import url
from .views import *


#2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

# Views should be nouns
# Forms and api endpoints should be verbs

urlpatterns = [
    url(r'^collections/$', CollectionListView.as_view()),
    url(r'^collections/(?P<pk>[-\w]+)/$', CollectionDetailView.as_view()),
    url(r'^collections/(?P<collection_id>[-\w]+)/create$', CollectionEntry.as_view()),
    # url(r'^collections/(?P<collection_id>[-\w]+)/data/(?P<pk>)$', DataEntry.as_view())
]

