from django.urls.conf import include

from recipe.views import TagViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()

router.register('tags', views.TagViewSet)
TagViewSet

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
