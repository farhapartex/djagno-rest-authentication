"""appAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .socialLogin import FacebookLogin, TwitterLogin
from rest_framework.routers import DefaultRouter
from django.conf import settings
from user import views as u_views

router = DefaultRouter()
router.register(r'profile', u_views.UserProfileAPiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('api/v1/accounts/', include('allauth.urls')),
    path('api/v1/rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/v1/rest-auth/twitter/',
         TwitterLogin.as_view(), name='twitter_login'),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/user-profile/list/', u_views.UserProfileListAPIView.as_view()),
    path('api/v1/', include(router.urls))
]


if settings.DEBUG:
    from django.conf.urls.static import static

    # Serve static and media files from development server
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
