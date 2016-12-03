from django.conf.urls import url
from .views import *


#2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

# Views should be nouns
# Forms and api endpoints should be verbs

urlpatterns = [
    url(r'^$', CodeSenseHome.as_view()),
]

