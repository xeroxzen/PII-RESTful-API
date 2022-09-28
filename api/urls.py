from rest_framework.routers import SimpleRouter
from .views import PiiViewSet

router = SimpleRouter()
router.register('api', PiiViewSet, basename='api')
urlpatterns = router.urls