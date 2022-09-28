from rest_framework.routers import SimpleRouter
from .views import UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')  
urlpatterns = router.urls