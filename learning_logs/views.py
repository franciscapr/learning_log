from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.
def index(request):
    """La pàgina de incio para Learning log."""
    return render(request, 'learning_logs/index.html')


# La vista de topics

def topics(request):
    """Muestra todos los temas."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Muestra todos los temas y todas sus entradas."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)