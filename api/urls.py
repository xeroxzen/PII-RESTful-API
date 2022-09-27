from rest_framework.routers import SimpleRouter
from .views import ApiViewSet

router = SimpleRouter()
router.register(r'', ApiViewSet, basename='api')
urlpatterns = router.urls