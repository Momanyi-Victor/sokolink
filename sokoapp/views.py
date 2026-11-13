from django.shortcuts import render
from sokoapp.models import *
from django.shortcuts import render,redirect

# Create your views here.
def error(request):
    return render(request, '404.html')

def details(request):
    return render(request, 'blog-details.html')


def blog(request):
    return render(request, 'blog.html')

def index(request):
    if request.method == 'POST':
        mycontact = Contact (
            name = request.POST['name'],
            email = request.POST['email'],
            message = request.POST['message'],
            subject = request.POST['subject'],
        )
        mycontact.save()
        return redirect('/')
    else:
        return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')


def show(request):
    all = Contact.objects.all()
    return render(request, 'show.html', { "all" : all})