from django.shortcuts import render
from django.http import HttpResponse
from .models import Superheroe
from .forms import TestForm
# Create your views here.


def home(request):
    superheroe  = Superheroe.objects.all()
    data = {
        'superheroe': superheroe 
    }
    return render(request, 'mi_app/home.html', data)

def test(request):
    data = {
        'form': TestForm()
    }

    if request.method == 'POST':
        formulario = TestForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "datos guardados"
        else:
            data["form"] = formulario

    return render(request, 'mi_app/test.html',data)
