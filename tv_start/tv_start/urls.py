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
from django.urls import path, include
from rest_framework import routers
from feedback.views import FeedbackView
from nard.views import BackgammonList, BackgammonViewSet
from sport_matches.views import *
from title.views import *

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'details', ArticleViewSet)

router2 = routers.DefaultRouter()
router2.register(r'matches_details', MatchViewSet)

router3 = routers.DefaultRouter()
router3.register(r'backgammon_details', BackgammonViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/v1/article/', include(router.urls)),
    path('api/v1/article/list/', ArticleList.as_view()),

    path('api/v1/feedback/', FeedbackView.as_view()),

    path('api/v1/matches/', include(router2.urls)),
    path('api/v1/matches/list/', MatchList.as_view()),

    path('api/v1/backgammon/', include(router3.urls)),
    path('api/v1/backgammon/list/', BackgammonList.as_view()),

    path('api/v1/auth/', include('rest_framework.urls')),

    path('', views.index)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
