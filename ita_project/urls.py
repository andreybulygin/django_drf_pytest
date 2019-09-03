from django.conf.urls import *

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
