"""Define padroes de URL para learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Pagina inicial 
    path('', views.index, name='index'),
    #Pagina de detalhes para um unico topico
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

]