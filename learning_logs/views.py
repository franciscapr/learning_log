from django.shortcuts import render

# Create your views here.
def index(request):
    """La pàgina de incio para Learning log."""
    return render(request, 'learning_logs/index.html')