from django.shortcuts import render

# Create your views here.
def index(request):
    datas = {

    }
    return render(request, 'pages/index.html')

def about(request):
    datas = {
        
    }
    return render(request, 'pages/about.html')

def service(request):
    datas = {
        
    }
    return render(request, 'pages/service.html')

def blog(request):
    datas = {
        
    }
    return render(request, 'pages/blog.html')

def single_blog(request):
    datas = {
        
    }
    return render(request, 'pages/single-blog.html')

def project(request):
    datas = {
        
    }
    return render(request, 'pages/project.html')

def appartment(request):
    datas = {
        
    }
    return render(request, 'pages/appartment.html')

def elements(request):
    datas = {
        
    }
    return render(request, 'pages/elements.html')

def contact(request):
    datas = {
        
    }
    return render(request, 'pages/contact.html')