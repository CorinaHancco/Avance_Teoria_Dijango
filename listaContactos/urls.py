"""listaContactos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from personas.views import personaCreateView, personaDeleteView, personaTestView, personasAnotherCreateView, personasListView, personasShowObject, searchForHelp
from inicio.views import anotherView, myHomeView
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('',myHomeView,name='Pagina de Inicio'),
    #path('another/',anotherView,),
    path('admin/', admin.site.urls),
    
    path('personas/',include('personas.urls')),
    #path('persona/',personaTestView,name='otro'),
    #path('add',personaCreateView,name='createPersona'),
    #path('search/',searchForHelp,name='buscar'),
    #path('anotherAdd',personasAnotherCreateView,name='OtroAgregarPersonas'),
    #path('personas/<int:myID>/',personasShowObject, name = 'browsing'),
    #path('personas/<int:myID>/delete/',personaDeleteView, name = 'deleting'),
    #path('personas/',personasListView, name = 'listing'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)