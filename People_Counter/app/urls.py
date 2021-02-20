from django.urls import path
from .views import video_streaming_view, index_view

urlpatterns = [
    path('',index_view,name='home'),
    path('live-stream/',video_streaming_view,name='live-stream'),
]