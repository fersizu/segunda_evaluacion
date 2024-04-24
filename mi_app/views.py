from django.shortcuts import render
from django.http import HttpResponse
from .models import Superheroe
from .forms import TestForm
from .models import Test
# Create your views here.


def home(request):
    return render(request, 'mi_app/home.html')


#def test(request):
#    data = {
#        'form': TestForm()
#        
#    }
#    superheroe = Superheroe.objects.all()
#
#    data1 = {
#        'superheroe': superheroe  # Pasar todos los superhéroes al contexto
#    }
#
#    if request.method == 'POST':
#        formulario = TestForm(data=request.POST)
#        if formulario.is_valid():
#            formulario.save()
#            data["mensaje"] = "datos guardados"
#            return render(request,'mi_app/resultados.html',data1,data)
#
#        else:
#            data["form"] = formulario
#
#    return render(request, 'mi_app/test.html',data)
def test(request):
    superheroe = Superheroe.objects.all()
    data = {
        'form': TestForm(),
       'superheroe': superheroe  # Pasar todos los superhéroes a resultados


    }
   

    if request.method == 'POST':
        formulario = TestForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "datos guardados"
            # Incluir los datos del formulario en el contexto
            data['formulario_data'] = formulario.cleaned_data
            return render(request, 'mi_app/resultados.html', data)

        else:
            data["form"] = formulario

    return render(request, 'mi_app/test.html', data)

def resultados(request):
    superheroe = Superheroe.objects.all()

    data = {
        'superheroe': superheroe  # Pasar todos los superhéroes al contexto
    }
    return render(request, 'mi_app/resultados.html', data)

