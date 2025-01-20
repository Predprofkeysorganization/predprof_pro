from rest_framework import routers
from user.apiapp import Application_ser

router = routers.DefaultRouter()
router.register('api/router', Application_ser, 'router')
urlpatterns = router.urls
