# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from core.models import Evento

#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
