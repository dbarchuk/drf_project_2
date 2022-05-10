from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register('posts', views.PostViewSet)

urlpatterns = router.urls
