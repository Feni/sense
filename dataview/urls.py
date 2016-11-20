from django.conf.urls import url
from django.contrib import admin
from .views import *


#2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

urlpatterns = [
    url(r'^$', home),
    url(r'^rows$', rows),
]
