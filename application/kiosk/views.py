from django.shortcuts import render

def index(request):
    context = {
        
    }
    return render(request, 'kiosk/index.html', context)

def register(request):
    context = {

    }
    return render(request, 'kiosk/register.html', context)