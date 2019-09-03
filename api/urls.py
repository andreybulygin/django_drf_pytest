from django.conf.urls import *

urlpatterns = [
    url('', include('api.v1.urls')),
]
