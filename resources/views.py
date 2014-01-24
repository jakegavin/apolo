from django.shortcuts import render
from resources.models import File

def index(request):
    files = File.objects.all()
    context = {'files': files}
    return render(request, 'resources/index.html', context)