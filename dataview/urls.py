from django.conf.urls import url
from .views import *


#2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

urlpatterns = [
    url(r'^$', CollectionListView.as_view()),
    url(r'^collections/(?P<pk>[-\w]+)/$', CollectionDetailView.as_view()),
    url(r'^new$', CollectionEntry.as_view())
]

