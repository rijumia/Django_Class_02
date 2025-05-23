from django.contrib import admin
from django.urls import path
from myProject.views import homePage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', homePage),
]
