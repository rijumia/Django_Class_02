from django.shortcuts import render, redirect

def homePage(request):
    return render(request, 'home.html')

def contactPage(request):
    return render(request, 'contact.html')

def signupPage(request):
    return render(request, 'signup.html')