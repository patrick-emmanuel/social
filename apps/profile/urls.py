from rest_framework.routers import DefaultRouter

from apps.profile import views

app_name = 'profile'

router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet, base_name='profile')
urlpatterns = router.urls
