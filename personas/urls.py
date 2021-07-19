from django.urls import path
from personas.views import (
    personaCreateView, 
    personaDeleteView, 
    personaTestView, 
    personasAnotherCreateView, 
    personasListView, 
    personasShowObject, 
    searchForHelp
)

from .views import (
    PersonaCreateView,
    PersonaDetailView,
    PersonaDeleteView,
    PersonaListView,
    PersonaQueryView,
    PersonaUpdateView,
)

app_name = 'personas'
urlpatterns = [
    #path('persona/',personaTestView,name='otro'),
    #path('add',personaCreateView,name='createPersona'),
    #path('search/',searchForHelp,name='buscar'),
    #path('anotherAdd',personasAnotherCreateView,name='OtroAgregarPersonas'),
    #path('<int:myID>/',personasShowObject, name = 'browsing'),
    #path('<int:myID>/delete/',personaDeleteView, name = 'deleting'),
    #path('',personasListView, name = 'listing'),

    #django5
    path('',PersonaListView.as_view(),name = 'persona-list'),
    path('<int:pk>/',PersonaDetailView.as_view(),name='persona-detail'),
    path('create/',PersonaCreateView.as_view(), name = 'persona-create'),
    path('<int:pk>/update/',PersonaUpdateView.as_view(), name = 'persona-create'),
    path('<int:pk>/delete/',PersonaDeleteView.as_view(), name = 'persona-confirm-delete'),

    path('query/',PersonaQueryView.as_view(), name ='persona-query'),

]
