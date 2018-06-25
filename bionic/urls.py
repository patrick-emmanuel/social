"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import (
    refresh_jwt_token,
    verify_jwt_token,
    ObtainJSONWebToken
)

from bionic import views
from bionic.auth import JWTSerializer

urlpatterns = [
    path('api/', include([
        path('admin/', admin.site.urls),
        path('docs/', include_docs_urls(title='Social API', description='RESTful API for Bionic Social')),

        path('', views.api_root),
        path('users/', include('apps.user.urls', namespace='users')),

        # Authentication routes.
        path('login', ObtainJSONWebToken.as_view(serializer_class=JWTSerializer)),
        path('api-token-refresh', refresh_jwt_token),
        path('api-token-verify', verify_jwt_token),
        path('docs/', include('drf_openapi.urls'))
    ]))
]

