from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'front/home.html')

def search_results(request):
    return render(request, 'front/search_results.html')
    
def property_details(request):
    return render(request, 'front/property_details.html')

def ad_register(request):
    return render(request, 'front/ad_register.html')

def login(request):
    return render(request, 'front/login.html')

def forgot_password(request):
    return render(request, 'front/forgot_password.html')

def reset_password(request):
    return render(request, 'front/reset_password.html')

def backoffice_main(request):
    return render(request, 'front/backoffice/main.html')

def backoffice_edit(request):
    return render(request, 'front/backoffice/edit.html')

def backoffice_add(request):
    return render(request, 'front/backoffice/add.html')