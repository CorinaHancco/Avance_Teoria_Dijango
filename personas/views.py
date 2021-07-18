from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm, RawPersonaForm

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto':obj,
    }
    return render(request,"personas/descripcion.html",context)


def personaCreateView(request):
    print(request)
    if request.method == 'POST':
        nombre = request.POST.get('q')
        print(nombre)
    #print('GET: ',request.GET)
    #print('POST: ',request.POST)
    
  #form = PersonaForm(request.POST or None)
    #if form.is_valid():
     #   form.save()
      #  form = PersonaForm() #blanquea los cambios

    context = {
       # 'form': form
    }
    return render(request,'personas/personasCreate.html',context)

def searchForHelp(request):
    return render(request,'personas/search.html',{})

def personasAnotherCreateView(request):
    form = RawPersonaForm()
    context = {
        'form':form,
    }
    return render(request,'personas/personasCreate.html',context)
