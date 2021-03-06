from rest_framework import routers
from api.v1.users import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
