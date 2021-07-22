from django.urls.conf import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()

router.register('ingredients', views.IngredientViewSet)
router.register('tags', views.TagViewSet)


app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
