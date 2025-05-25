from django.contrib import admin
from django.urls import path
from myProject.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', homePage),
    path('contact', contactPage),
    path('signup', signupPage),
    path('viewStudent', viewStudentPage),
    path('viewCourse', coursePage),
]
