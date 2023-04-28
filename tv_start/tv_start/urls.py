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
from sport_matches.views import MatchViewSet, MatchList
from title.views import *

#
router = routers.DefaultRouter()
router.register(r'details', ArticleViewSet)
#
router2 = routers.DefaultRouter()
router2.register(r'matches_details', MatchViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/v1/article/', include(router.urls)),
    path('api/v1/article/list/', ArticleList.as_view()),

    path('api/v1/feedback/', FeedbackView.as_view()),

    path('api/v1/matches/', include(router2.urls)),
    path('api/v1/matches/list/', MatchList.as_view()),
]