from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from photos.api import PhotoViewSet
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView

router = DefaultRouter()
router.register('api/1.0/photos', PhotoViewSet, basename='api_photos_')

urlpatterns = [
    path('create/', PhotoCreationView.as_view(), name='photos_create'),
    path('photos/', PhotoListView.as_view(), name='photos_my_photos'),
    re_path(r'^photos/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    path('', HomeView.as_view(), name='photos_home'),

    path('', include(router.urls))
]