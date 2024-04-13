"""Define padroes de URL para learning_logs"""

from django.urls import path 

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Pagina inicial 
    path('', views.index, name='index'),
    #pagina que mostra todos os topicos 
    path('topics/', views.topics, name='topics'),
    #pagina de detalhes para um unico topico
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Pagina para adicionar um topico novo 
    path('new_topic/', views.new_topic, name='new_topic'),
    #Pagina para adicionar uma entrada nova
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    #path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]