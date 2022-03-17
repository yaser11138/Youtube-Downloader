from django.contrib import admin
from django.urls import path
from youtubedownloader import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.download_video, name='download'),
]
