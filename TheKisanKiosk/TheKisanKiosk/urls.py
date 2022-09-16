"""TheKisanKiosk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from register.views import apiregister, register
from base.views import homepage
from login.views import login, logout
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('', homepage, name='homepage'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('role/', include('rolemanager.urls')),
    path('profile/',include('profilemanager.urls')),
    path('posts/',include('posthandler.urls')),
    path('comments/',include('commenthandler.urls')),
    path('marketplace/',include('listingmanager.urls')),
    path('order/',include('ordermanager.urls')),
    path('likes/',include('likehandler.urls')),
    path('apilogin/',include('login.urls')),
    path('apiregister/',apiregister.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
