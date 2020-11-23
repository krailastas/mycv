from rest_framework.routers import SimpleRouter

from .views import (
    MainViewSet, JobsViewSet)

router = SimpleRouter(trailing_slash=False)
router.register('main', MainViewSet, basename='main')
router.register('jobs', JobsViewSet, basename='jobs')

urlpatterns = router.urls
