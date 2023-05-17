from django.urls import path, include

from content.views import FeedUpload

urlpatterns = [
    path('feed', FeedUpload.as_view(), name='feed'),
]