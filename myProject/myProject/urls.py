from django.contrib import admin
from django.urls import path
from myProject.views import homePage, contactPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', homePage),
    path('contact', contactPage),
]
