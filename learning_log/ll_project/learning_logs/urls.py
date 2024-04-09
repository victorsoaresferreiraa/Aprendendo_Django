"""Define padroes de URL para learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Pagina inicial 
    path('', views.index, name='index')
]