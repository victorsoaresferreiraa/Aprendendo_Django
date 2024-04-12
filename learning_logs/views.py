from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

def index(request):
    """A pagina inicial para o registro de Aprendizagem"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os topicos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Mostra um unico topico e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adiciona um topico novo"""
    if request.method != 'POST':
        # nenhuma dado enviado, cria um formulario em branco.
        form = TopicForm()
    else:
        # dadps Post enviados, processa os dados .
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)  