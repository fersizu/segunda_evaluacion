from django.shortcuts import render
from django.http import HttpResponse
from .models import Superheroe
# Create your views here.


def home(request):
    superheroe  = Superheroe.objects.all()
    data = {
        'superheroe': superheroe 
    }
    return render(request, 'mi_app/home.html', data)

def test(request):
    return render(request, 'mi_app/test.html')