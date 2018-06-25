from django.urls import path, include
from apps.user import views

app_name = 'user'

urlpatterns = [
    path('register', views.UserCreateView.as_view(), name='user-create'),
    path('', views.UserListView.as_view(), name='user-list'),
    path('<str:username>', views.UserDetailView.as_view(), name='user-detail'),
    path('update', views.UserUpdateView.as_view(), name='user-update'),

    path('', include('apps.profile.urls')),
]
