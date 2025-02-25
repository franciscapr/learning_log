from django.shortcuts import render
from .models import Topic

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