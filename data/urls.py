from rest_framework.routers import SimpleRouter

from .views import (
    MainViewSet)

router = SimpleRouter(trailing_slash=False)
router.register('main', MainViewSet, basename='main')

urlpatterns = router.urls
