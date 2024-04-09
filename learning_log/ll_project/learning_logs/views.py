from django.shortcuts import render

# Create your views here.

def index(request):
    """A pagina inicial para o registro de Aprendizagem"""
    return render(request, 'learning_logs\index.html')