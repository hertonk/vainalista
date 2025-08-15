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