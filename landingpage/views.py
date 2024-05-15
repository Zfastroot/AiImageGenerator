from django.shortcuts import render

def index(request):
    return render(request , 'landingpage/index.html')

def about(request):
    return render(request, 'landingpage/about.html')

def service(request):
    return render(request, 'landingpage/service.html')

def team(request):
    return render(request, 'landingpage/team.html')

def contact(request):
    return render(request, 'landingpage/contact.html')

def demo(request):
    return render(request, 'landingpage/demo.html')