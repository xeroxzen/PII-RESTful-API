from rest_framework.routers import SimpleRouter
from .views import PiiViewSet

router = SimpleRouter()
router.register('pii', PiiViewSet, basename='pii')
urlpatterns = router.urls