from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .yasg import urlpatterns as yasg_url
from women.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', WomenAPIList.as_view()),  # Используем WomenAPIList для GET-запросов
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),  # Используем WomenAPIUpdate для PUT-запросов
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),  # Используем WomenAPIDestroy для GET, PUT, PATCH, DELETE -запросам

#маршруты по djoser
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

#маршруты по JWT(json web token)
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
