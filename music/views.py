from django.shortcuts import render
from .models import Album, UserMessage

def home(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {'albums': albums})

def about(request):
    return render(request, 'about.html')

def contact(request):
    success = False

    if request.method == 'POST':
        UserMessage.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        success = True

    return render(request, 'contact.html', {'success': success})
