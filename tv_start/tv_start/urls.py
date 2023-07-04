"""
URL configuration for sitedjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from feedback.views import FeedbackView
from nard.views import BackgammonList, BackgammonViewSet
from sport_matches.views import *
from title.views import *
from infos.views import *
from services.views import *

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'details', ArticleViewSet)

router2 = routers.DefaultRouter()
router2.register(r'matches_details', MatchViewSet)

router3 = routers.DefaultRouter()
router3.register(r'backgammon_details', BackgammonViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for your project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),

    path('api/v1/article/', include(router.urls)),
    path('api/v1/article/list/', ArticleList.as_view()),

    path('api/v1/feedback/', FeedbackView.as_view()),

    path('api/v1/matches/', include(router2.urls)),
    path('api/v1/matches/list/', MatchList.as_view()),

    path('api/v1/backgammon/', include(router3.urls)),
    path('api/v1/backgammon/list/', BackgammonList.as_view()),

    path('api/v1/infos/', InfoView.as_view()),
    path('api/v1/services/', ServicesView.as_view()),



    # path('api/v1/auth/', include('rest_framework.urls')),


    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# AIzaSyBVtWiHEckJ9kwzJozbqVCaZ2DYok_9XmY
