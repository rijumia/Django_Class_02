from django.shortcuts import render, redirect
from myApp.models import *

def homePage(request):
    return render(request, 'home.html')

def contactPage(request):
    return render(request, 'contact.html')
def loginPage(request):
    return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = userModel.objects.get(username=username, password=password)
            return redirect('viewStudent')
        except userModel.DoesNotExist:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error': error_message})

    return render(request, 'login.html')

def signupPage(request):
    return render(request, 'signup.html')

def viewStudentPage(request):

    studentData = studentModel.objects.all()

    context = {
        'students': studentData,
    }

    return render(request, 'viewStudent.html', context)


def coursePage(request):
    courseData = courseModel.objects.all()

    context = {
        'courses': courseData,
    }

    return render(request, 'viewCourse.html', context)