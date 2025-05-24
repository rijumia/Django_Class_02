from django.contrib import admin
from django.urls import path
from myProject.views import homePage, contactPage, signupPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', homePage),
    path('contact', contactPage),
    path('signup', signupPage),
]
