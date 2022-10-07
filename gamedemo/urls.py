"""gamedemo URL Configuration

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
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView
from graph.schema import schema

from rest_framework.routers import DefaultRouter
from game.views import GameViewSet
from player.views import PlayerViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'games', GameViewSet, basename="games")
router.register(r'players', PlayerViewSet, basename="players")

from auth.views import CustomAuthToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql", csrf_exempt(
        FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),
    path("auth/", CustomAuthToken.as_view()),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
