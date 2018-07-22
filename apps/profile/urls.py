from rest_framework.routers import DefaultRouter

from apps.profile import views

app_name = 'profile'

router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet, base_name='profile')
router.register(r'profile_image', views.ProfilePhotoViewSet, base_name='profile_image')
urlpatterns = router.urls
